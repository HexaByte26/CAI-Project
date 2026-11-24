from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
  return render_template('front_page.html')

@views.route('/landing-page')
def front_page():
  return render_template('landing_page.html')

@views.route('/home')
def home():
  return render_template('home.html')

@views.route('/topic')
def sequential_circuit():
  return render_template('topic.html')

@views.route('/sub-topic-<number>')
def sub_topic(number):
  if number > 2 or number < 1:
    return
  
  return render_template(f'sub_topic_{number}.html')

@views.route('/user-<tup_id>')
def user(tup_id):
  return render_template('dashboard.html')