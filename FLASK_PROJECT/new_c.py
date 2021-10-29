from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@localhost/flask1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
from model import *
class employeeddd(db.Model):
    ad = db.Column('emp_id', db.Integer(), primary_key=True)

    name=db.Column('emp_name',db.String(30))
    mobile = db.Column('emp_mobile',db.BigInteger())

if __name__=='__main__':
    db.create_all()