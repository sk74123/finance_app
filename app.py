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


#DB Model for User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String(50), nullable=False)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'GET':
        return "Hello World!!"
    if request.method == 'POST':
        print(request)
        print(dir(request))
        print(request.body)
        error = {
            'msg': ' POST is not allowed'
        }
        error = json.dumps(error)
        return error


if __name__ == '__main__':
    app.run(debug=True)
