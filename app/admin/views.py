from flask import render_template, request, redirect, url_for
from . import admin
from app.utils.utils import login_required
from app.utils.enums import PaymentModes, MotorCoverTypes, \
    QuotationTypes, PaymentPlans
from app.controllers import get_customers, get_customer_info, \
    update_customer_status, get_items_of_sale, create_item_of_sale, \
    get_invoices, create_invoice, create_payment, get_payments, \
    create_motor_private_quote, get_quote, update_quote
from .forms import SaleItemForm, CustomerInvoiceForm, \
    CustomerInvoicePaymentForm, MotorQuotation


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
    customer_invoice_form.item.choices = [
        (item.id, "%s - %s" % (item.name, item.category)) for item in get_items_of_sale()
    ]
    customer_invoice_payment_form = CustomerInvoicePaymentForm()
    customer_invoice_payment_form.payment_mode.choices = [
        (payment_mode.name, payment_mode.name) for payment_mode in PaymentModes
    ]
    customer_motor_private_quotation_form = MotorQuotation(
        quotation_type=QuotationTypes.MOTOR_PRIVATE.name
    )
    customer_motor_private_quotation_form.motor_cover_type.choices = [
        (cover_type.name, cover_type.name) for cover_type in MotorCoverTypes
    ]
    customer_motor_private_quotation_form.payment_plan.choices = [
        (payment_plan.name, payment_plan.name) for payment_plan in PaymentPlans
    ]
    customer_payload = dict(
        customer_invoice_form=customer_invoice_form,
        customer_invoice_payment_form=customer_invoice_payment_form,
        customer_motor_private_quotation_form=customer_motor_private_quotation_form
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
        quotation_type=request.form['quotation_type'],
        sum_insured=request.form['sum_insured'],
        motor_cover_type=request.form['motor_cover_type'],
        motor_use=request.form['motor_use'],
        vehicle_model=request.form['vehicle_model'],
        year_of_manufacture=request.form['year_of_manufacture'],
        cover_start_date=request.form['cover_start_date'],
        payment_plan=request.form['payment_plan'],
        customer_id=customer_id
    )
    create_motor_private_quote(quotation_payload)
    return redirect(url_for('admin.customer', customer_id=customer_id))


@admin.route(
    '/update-customer-quotation/<string:quotation_id>', 
    methods=['GET', 'POST']
)
@login_required
def update_customer_quotation(quotation_id):
    quotation_type = request.args.get('quotation-type', '')
    quotation = get_quote(quotation_type, quotation_id)
    print(quotation.payment_plan)
    form = MotorQuotation(obj=quotation)
    form.motor_cover_type.choices = [
        (cover_type, cover_type.value) for cover_type in MotorCoverTypes
    ]
    print(form.quotation_type.data)
    form.payment_plan.choices = [
        (payment_plan, payment_plan.value) for payment_plan in PaymentPlans
    ]
    if form.validate_on_submit():
        print("COV", type(form.payment_plan.data))
        quotation_payload = dict(
            # quotation_type=form.quotation_type.data,
            sum_insured=form.sum_insured.data,
            motor_cover_type=form.motor_cover_type.data,
            motor_use=form.motor_use.data,
            vehicle_model=form.vehicle_model.data,
            year_of_manufacture=form.year_of_manufacture.data,
            cover_start_date=form.cover_start_date.data,
            payment_plan=form.payment_plan.data
        )
        update_quote(quotation_type, quotation_id, quotation_payload)
        redirect(url_for('admin.customer', customer_id=quotation.customer_id))
    return render_template(
        "admin/update-quotation.html", 
        form=form, 
        action='/update-customer-quotation/%s?quotation-type=%s' % (
            quotation_id, quotation_type
        ),
        customer_id=quotation.customer_id
    )


@admin.route('/create-customer-invoice/<string:customer_id>', methods=['POST'])
@login_required
def create_customer_ivoice(customer_id):
    invoice_payload = dict(
        item=request.form['item'],
        price=request.form['price'],
        customer=customer_id,
        due_at=request.form['due_at'],
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
    quotations = {}  # get_quotations()
    return render_template("admin/quotations.html", quotations=quotations)


@admin.route('/payments', methods=['GET'])
@login_required
def payments():
    payments = get_payments()
    return render_template("admin/payments.html", payments=payments)


@admin.route('/covers', methods=['GET'])
@login_required
def covers():
    return render_template("admin/covers.html")
