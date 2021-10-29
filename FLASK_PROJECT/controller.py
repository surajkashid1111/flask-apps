from config import app
from flask import request,render_template

'''
@app.route('/',methods= ['GET'])
def welcome_page():
    #print(request.args)
    return render_template('employee.html')



@app.route('/',methods =['POST'])  # IF we written post method inside the html also
def save_or_update_employee():
    print('inside the emp info')
    print(request.form)
    return render_template('employee.html')'''

@app.route('/index',methods =['POST','GET'])  # if we written two method same time it will serve these two method at time.
def save_or_update_employee_in_both():
    print('inside the emp info both')
    formdata = None
    if request.method =='GET':
        print('data is inside get method -url')
        formdata = request.args
    else:
        print('data inside the post method')
        formdata= request.form
        print(formdata)
    return render_template('employee.html')


@app.route('/employee/delete/')
def delete_employee():
    pass


@app.route('/employee/fetch')
def fetch_employee_for_edit():
    pass

#if __name__=='__main__':
    app.run(debug=True)
