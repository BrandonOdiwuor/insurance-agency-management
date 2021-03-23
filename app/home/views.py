from flask import render_template
from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template("home/index.html")


@home.route('/about-us')
def about_us():
    """
    Render the about_us template on the /about-us route
    """
    return render_template('home/about_us.html')

@home.route('/contact-us')
def contact_us():
    """
    Render the contact_us template on the /contact-us route
    """
    return render_template('home/contact_us.html')