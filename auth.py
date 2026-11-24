from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    tup_id = request.form.get('tup_id')
    password = request.form.get('password')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    tup_id = request.form.get('tup_id')
    gsfe_email = request.form.get('gsfe_email')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')