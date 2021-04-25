from flask import render_template, request, redirect, url_for
from . import admin
from app.utils.utils import login_required, save_file
from app.utils.enums import PaymentModes, MotorPolicyTypes, \
    ProductTypes, PaymentPlans, PolicyStatus, InvoiceStatus
from app.controllers import get_customers, get_customer_info, \
    update_customer_status, get_customer_policies, create_item_of_sale, \
    get_invoices, create_invoice, create_payment, get_payments, \
    create_motor_quote, get_quote, update_quote, get_quotes, \
    create_policy, get_items_of_sale, get_policies, get_policy, update_policy
from .forms import SaleItemForm, CustomerInvoiceForm, MotorQuotationForm, \
    CustomerInvoicePaymentForm, MotorPolicyForm
from .utils import motorQuotationForm, motorPolicyForm


@admin.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template("admin/dashboard.html")


@admin.route('/customers', methods=['GET'])
@login_required
def customers():
    customers = get_customers()
    return render_template("admin/customers.html", customers=customers)


@admin.route('/customer/<string:customer_id>', methods=['GET'])
@login_required
def customer(customer_id):
    customer_info = get_customer_info(customer_id)
    customer_invoice_form = CustomerInvoiceForm()
    customer_invoice_form.policy_id.choices = [
        (
            policy.id, "%s - %s" % (policy.product_type.value,
                                    "{:,}".format(policy.premium))
        ) for policy in get_customer_policies(customer_id)
    ]
    customer_invoice_payment_form = CustomerInvoicePaymentForm()
    customer_invoice_payment_form.payment_mode.choices = [
        (payment_mode.name, payment_mode.value) for payment_mode in PaymentModes
    ]
    customer_motor_private_quotation_form = motorQuotationForm(
        ProductTypes.MOTOR_PRIVATE
    )
    customer_motor_commercial_quotation_form = motorQuotationForm(
        ProductTypes.MOTOR_COMMERCIAL
    )
    customer_private_motor_policy_form = motorPolicyForm(
        MotorPolicyForm(product_type=ProductTypes.MOTOR_PRIVATE)
    )
    customer_commercial_motor_policy_form = motorPolicyForm(
        MotorPolicyForm(product_type=ProductTypes.MOTOR_COMMERCIAL)
    )
    customer_payload = dict(
        customer_invoice_form=customer_invoice_form,
        customer_invoice_payment_form=customer_invoice_payment_form,
        customer_motor_private_quotation_form=customer_motor_private_quotation_form,
        customer_motor_commercial_quotation_form=customer_motor_commercial_quotation_form,
        customer_private_motor_policy_form=customer_private_motor_policy_form,
        customer_commercial_motor_policy_form=customer_commercial_motor_policy_form
    )
    customer_payload.update(customer_info)
    return render_template(
        "admin/customer.html",
        **customer_payload
    )


@admin.route('/create-customer-quotation/<string:customer_id>', methods=['POST'])
@login_required
def create_customer_quotation(customer_id):
    quotation_payload = dict(
        product_type=ProductTypes[
            request.form['product_type'].split('.')[1]
        ],
        sum_insured=request.form['sum_insured'],
        recent_profesional_evaluation=True if request.form[
            'recent_profesional_evaluation'
        ] == 'y' else False,
        motor_policy_type=request.form['motor_policy_type'],
        motor_use=request.form['motor_use'],
        motor_model=request.form['motor_model'],
        motor_make=request.form['motor_make'],
        motor_year_of_manufacture=request.form['motor_year_of_manufacture'],
        policy_start_date=request.form['policy_start_date'],
        payment_plan=request.form['payment_plan'],
        customer_id=customer_id
    )
    if quotation_payload['product_type'] == ProductTypes.MOTOR_PRIVATE or \
            quotation_payload['product_type'] == ProductTypes.MOTOR_COMMERCIAL:
        create_motor_quote(quotation_payload)
    return redirect(url_for('admin.customer', customer_id=customer_id))


@admin.route(
    '/update-customer-quotation/<string:quotation_id>',
    methods=['GET', 'POST']
)
@login_required
def update_customer_quotation(quotation_id):
    quotation_type = request.args.get('quotation-type', '')
    quotation = get_quote(quotation_type, quotation_id)
    form = MotorQuotationForm(obj=quotation)
    form.motor_policy_type.choices = [
        (policy_type, policy_type.value) for policy_type in MotorPolicyTypes
    ]
    form.motor_year_of_manufacture.choices = [
        (year, year) for year in range(1995, 2022)
    ]
    form.payment_plan.choices = [
        (payment_plan, payment_plan.value) for payment_plan in PaymentPlans
    ]
    if form.validate_on_submit():
        quotation_payload = dict(
            product_type=quotation.product_type.name,
            sum_insured=request.form['sum_insured'],
            recent_profesional_evaluation=True if request.form[
                'recent_profesional_evaluation'
            ] == 'y' else False,
            motor_policy_type=MotorPolicyTypes[
                request.form['motor_policy_type'].split('.')[1]
            ],
            motor_use=request.form['motor_use'],
            motor_model=request.form['motor_model'],
            motor_make=request.form['motor_make'],
            motor_year_of_manufacture=request.form['motor_year_of_manufacture'],
            policy_start_date=request.form['policy_start_date'],
            payment_plan=PaymentPlans[
                request.form['payment_plan'].split('.')[1]
            ]
        )
        update_quote(quotation_id, quotation_payload)
        return redirect(url_for('admin.customer', customer_id=quotation.customer_id))
    return render_template(
        "admin/update-quotation.html",
        form=form,
        action='/update-customer-quotation/%s?quotation-type=%s' % (
            quotation_id, quotation_type
        ),
        customer_id=quotation.customer_id
    )


@admin.route('/create-customer-policy/<string:customer_id>', methods=['POST'])
@login_required
def create_customer_policy(customer_id):
    policy_payload = dict(
        product_type=ProductTypes[request.form['product_type'].split('.')[1]],
        sum_insured=request.form['sum_insured'],
        recent_profesional_evaluation=True if request.form[
            'recent_profesional_evaluation'
        ] == 'y' else False,
        motor_policy_type=MotorPolicyTypes[request.form['motor_policy_type']],
        motor_use=request.form['motor_use'],
        motor_model=request.form['motor_model'],
        motor_make=request.form['motor_make'],
        motor_year_of_manufacture=request.form['motor_year_of_manufacture'],
        policy_start_date=request.form['policy_start_date'],
        payment_plan=PaymentPlans[request.form['payment_plan']],
        policy_status=PolicyStatus[request.form['policy_status']],
        policy_expiry_date=request.form['policy_expiry_date'],
        policy_number=request.form['policy_number'],
        policy_underwriter=request.form['policy_underwriter'],
        log_book_attachment=save_file(request.files['log_book_attachment']),
        customer_id=customer_id
    )
    create_policy(policy_payload)
    return redirect(url_for('admin.customer', customer_id=customer_id))


@admin.route(
    '/update-customer-policy/<string:policy_id>',
    methods=['GET', 'POST']
)
@login_required
def update_customer_policy(policy_id):
    policy = get_policy(policy_id)
    policy.policy_status = policy.policy_status.name
    policy.payment_plan = policy.payment_plan.name
    policy.motor_policy_type = policy.motor_policy_type.name
    form = motorPolicyForm(MotorPolicyForm(obj=policy))
    if form.validate_on_submit():
        policy_payload = dict(
            sum_insured=request.form['sum_insured'],
            recent_profesional_evaluation=True if request.form[
                'recent_profesional_evaluation'
            ] == 'y' else False,
            motor_policy_type=MotorPolicyTypes[
                request.form['motor_policy_type']
            ],
            motor_use=request.form['motor_use'],
            motor_model=request.form['motor_model'],
            motor_make=request.form['motor_make'],
            motor_year_of_manufacture=request.form['motor_year_of_manufacture'],
            policy_start_date=request.form['policy_start_date'],
            payment_plan=PaymentPlans[
                request.form['payment_plan']
            ],
            policy_status=PolicyStatus[
                request.form['policy_status']
            ]
        )
        update_policy(policy_id, policy_payload)
        return redirect(url_for('admin.customer', customer_id=policy.customer_id))
    return render_template(
        "admin/update-policy.html",
        form=form,
        action='/update-customer-policy/%s' % (policy_id),
        customer_id=policy.customer_id
    )

@admin.route('/create-customer-invoice/<string:customer_id>', methods=['POST'])
@login_required
def create_customer_ivoice(customer_id):
    invoice_payload = dict(
        policy_id=request.form['policy_id'],
        amount=request.form['amount'],
        customer_id=customer_id,
        due_date=request.form['due_date'],
        status=InvoiceStatus.ACTIVE
    )
    create_invoice(invoice_payload)
    return redirect(url_for('admin.customer', customer_id=customer_id))


@admin.route(
    '/create-customer-invoice-payment/<string:customer_id>', methods=['POST']
)
@login_required
def create_customer_ivoice_payment(customer_id):
    invoice_payment_payload = dict(
        invoice=request.form['invoice_id'],
        amount=request.form['amount'],
        payment_mode=request.form['payment_mode'],
    )
    create_payment(invoice_payment_payload)
    return redirect(url_for('admin.customer', customer_id=customer_id))


@admin.route('/update-customer-status/<string:customer_id>', methods=['GET'])
@login_required
def change_customer_status(customer_id):
    update_customer_status(customer_id)
    return redirect(url_for('admin.customer', customer_id=customer_id))


@admin.route('/products', methods=['GET'])
@login_required
def products():
    products = get_items_of_sale()
    return render_template("admin/products.html", products=products)


@admin.route('/register-product', methods=['GET', 'POST'])
@login_required
def register_product():
    form = SaleItemForm()

    if form.validate_on_submit():
        sale_item_payload = {
            'name': form.name.data,
            'category': form.category.data,
            'price': form.price.data
        }
        create_item_of_sale(sale_item_payload)
        return redirect(url_for('admin.products'))
    return render_template("admin/register-product.html", form=form)


@admin.route('/invoices', methods=['GET'])
@login_required
def invoices():
    invoices = get_invoices()
    return render_template("admin/invoices.html", invoices=invoices)


@admin.route('/new-invoice', methods=['GET', 'POST'])
@login_required
def new_invoice():
    form = SaleItemForm(request.form)

    # if form.validate_on_submit():
    #     sale_item_payload = {
    #         'name': form.name.data,
    #         'category': form.category.data,
    #         'price': form.price.data
    #     }
    #     create_item_of_sale(sale_item_payload)
    #     return redirect(url_for('app.products'))
    return render_template("forms/invoice.html", form=form)


@admin.route('/quotations', methods=['GET'])
@login_required
def quotations():
    quotations = get_quotes()
    return render_template("admin/quotations.html", quotations=quotations)


@admin.route('/payments', methods=['GET'])
@login_required
def payments():
    payments = get_payments()
    return render_template("admin/payments.html", payments=payments)


@admin.route('/policies', methods=['GET'])
@login_required
def policies():
    policies = get_policies()
    return render_template("admin/policies.html", policies=policies)
