from flask import render_template
from . import customer
from utils.utils import login_required


@customer.route('/customer-dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template("customer/dashboard.html")