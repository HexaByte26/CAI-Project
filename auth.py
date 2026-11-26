from flask import Blueprint, render_template, request, flash, redirect, url_for
from db import DBMS

dbms = DBMS()
auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    tupc_id = request.form.get('tupc_id')
    password = request.form.get('password')

    dbms.connect()
    if dbms.fetch_profile(tupc_id, password):
      return redirect(url_for('/'))

    return render_template('login.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    tupc_id = request.form.get('tupc_id')
    gsfe_email = request.form.get('gsfe_email')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    school_code, year, identfication = tupc_id.split("-")

    if '@' not in gsfe_email:
      flash("invalid email")
      return render_template('signup.html')

    at_symbol_index = gsfe_email.index('@')
    email_format = gsfe_email[at_symbol_index::]

    if email_format != "@gsfe.tupcavite.edu.ph":
      flash("invalid email")
      return render_template('signup.html')

    if school_code == "TUPC":
      flash("invalid TUP school code")
      return render_template('signup.html')

    if not year.isdigit():
      flash("invalid year")
      return render_template('signup.html')

    if len(identfication) < 4:
      flash("invalid identification code")
      return render_template('signup.html')

    if len(fname) < 1 or len(lname) < 1:
      flash("First Name and Last Name length must be 2 or greater")
      return render_template('signup.html')

    if password != confirm_password:
      flash("password and confirm password is not match")
      return render_template('signup.html')

    if password < 7:
      flash("password length must be 8 or greater")
      return render_template('signup.html')

    dbms.connect()
    dbms.save_profile((tupc_id, gsfe_email, fname, lname, password))

    return redirect(url_for('login'))

  return render_template('signup.html')