from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'groupofalfonso'

from auth import auth
from views import views

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(views, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)