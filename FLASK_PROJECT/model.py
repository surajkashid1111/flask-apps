from config import db

class Employee(db.Model):
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name', db.String(30))
    mobile= db.Column('emp_mobile', db.BigInteger()) #phone number always require bigint to hold phone number.
    gender= db.Column('emp_gender', db.String(30))
    roles = db.Column('emp_roles', db.String(30))
    address = db.Column('emp_address', db.String(30))
    exp = db.Column('emp_exp', db.Integer())        #exprience given---> value will be taken as input which 1 for 0-3 like that.
    salary = db.Column('emp_salary', db.Float())
    skills = db.Column('emp_skills', db.String(30))

if __name__ == '__main__':
    db.create_all()