from flask import Flask, render_template,request, url_for
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

""" Below, I was gonna use SQLAlchemy instead of MySQL--  """
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
""" 
MySQL seems like it would be more expansive. I don't know if the way to create
Models are the same. So I just commented out this block of code"""
# class Register(db.Model):
#     id = db.Column()
#     username = db.Column(db.String(20), nullable=False, primary_key=True)
#     password = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)


#Home Page
@app.route("/")
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html')

#Registration Page
@app.route('/registration')
def registration():
    return render_template('registration.html')

""" Login Page 
Is this necessary? I feel like search And Login should be on the homepage
But if the users search, and try to download without being registered, it wouldn't
Be cool to take them back to the homepage. So... """
@app.route('/login')
def user(name):
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)