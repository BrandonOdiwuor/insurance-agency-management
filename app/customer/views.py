from flask import render_template, session
from . import customer
from app.utils.utils import login_required, decode_token
from app.controllers import get_customer_info


@customer.route('/customer-dashboard', methods=['GET'])
@login_required
def dashboard():
    customer_id = decode_token(session['authorization'])['uid']
    customer_payload = get_customer_info(customer_id)
    return render_template("customer/dashboard.html", **customer_payload)