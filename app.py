from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

# Creating instance of SQLalchemy
db = SQLAlchemy()

#Creating instance of Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


# DB Model for User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String(50), nullable=False)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/user',methods=['GET','POST','PUT','DELETE'])
def getUser():
    
    if request.method == 'GET':
        user = User.query.all()
        for u in user:
            print(u.username)
            print(u.email)
        msg = {'msg' : 'get_request'}
        msg = json.dumps(msg)
        return msg
    
    if request.method == 'POST':
        data = json.loads(request.data)
        username = data["username"]
        email = data["email"]
        password = data["password"]
        print(username)
        print(email)
        print(password)
        user = User(username = username, email = email, password = password)
        db.session.add(user)
        db.session.commit()
        msg = {"test" : "test_msg"}
        msg = json.dumps(msg)
        return msg

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return "Hello World!!"

if __name__ == '__main__':
    app.run(debug=True)
