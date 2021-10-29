
from config import *
from flask import request,render_template
from model import Employee

@app.route('/',methods=['GET'])
def welcome_page():
    return render_template('employee.html',emplist = Employee.query.all())

@app.route('/save',methods=['POST'])
def save_employee_info():
    formdata = request.form     #from this data will come to the server--->but not decided to upload on browser or not
                                # if data is proper data will be uploaded.

    msg = None
    eid = int(formdata.get('id'))
    dbemp= Employee.query.filter_by(id=eid).first()
    print(dbemp)
    if dbemp:
        dbemp.name = formdata.get('name')
        dbemp.mobile = formdata.get('mobile')
        db.session.commit()    #update --> u can write all other field
        msg = 'record is updated successfully'
    else:
        emp = Employee(id = formdata.get('id'),name =formdata.get('name'),mobile =formdata.get('mobile') ,gender = formdata.get('gender'),roles=formdata.get('roles'),address= formdata.get('address'),exp=formdata.get('exp'),salary= formdata.get('salary'),skills = formdata.get('skills'))
        db.session.add(emp)   #will fire insert query.
        db.session.commit()
        msg = 'record created succefully...!'
    return render_template('employee.html',resp=msg,emplist = Employee.query.all())

if __name__=='__main__':
    app.run(debug=True)
