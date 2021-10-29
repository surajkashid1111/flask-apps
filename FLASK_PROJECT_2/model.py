from config import *
class Generic(db.Model):
    __abstract__=True   # for to said this is not to table --> it only base error
    created_on = db.Column(db.DateTime,server_default = db.func.now())             # this date and time where details are uploaded.or created
    update_on = db.Column(db.DateTime, server_default=db.func.now(),server_onupdate= db.func.now())  #updated.
    active = db.Column('active',db.String(10),default ='Y')


class Userinfo(Generic):
    __tablename__= 'user_details'
    id = db.Column('id',db.Integer(),primary_key = True)
    first_name = db.Column('first_name',db.String(100))
    last_name = db.Column('last_name',db.String(100))
    email = db.Column('email',db.String(100),unique=True,nullable = False)
    gender = db.Column('gender',db.String(100))
    mobile = db.Column('mobile',db.BigInteger(),unique=True)
    loginref= db.relationship('LoginInfo',uselist=False,backref= 'userreff')
    #this is opposite reference of foreign key of ^^^^^for 1-1 connection
    roleId= db.Column(db.ForeignKey('role_details.id'),unique= False,nullable=True)

class LoginInfo(Generic):
    __tablename__ = 'login_details'
    id = db.Column('id',db.Integer(),primary_key = True)
    username = db.Column('username',db.String(100),unique=True,nullable = False)
    password = db.Column('password',db.String(100))

    userid= db.Column('userid',db.ForeignKey('user_details.id'),unique=True,nullable = False)
    #this is foreign key of userinfo to make 1-1 connection.


class ProductInfo(Generic):
    __tablename__ = 'product_details'
    id = db.Column('id',db.Integer(),primary_key = True)
    name = db.Column('name',db.String(100))
    price = db.Column('price',db.Float())
    qty = db.Column('qty',db.Integer())
    vendor = db.Column('vendor',db.String(100))

class RoleInfo(Generic):
    __tablename__ = 'role_details'
    id = db.Column('id',db.Integer(),primary_key=True)
    name = db.Column('role_name',db.String(100))
    userref= db.relationship(Userinfo,uselist=True,lazy=True,backref= "roleref ")
    #here refernce bellow that so userinfo wriiten directly without qoutes.
#may be lot of user have same role.^^ so that use the uselist.

import time
def initialize_system(reset=False):# flase means by default it is false---> if want true mention at the time of callin
    if reset:    # to reset all data into to the database this command is used.
        db.drop_all()
        print('removed entire table and going to create fresh one..')


    db.create_all()            #it will create the table

    user= Userinfo.query.filter_by(id=99).first()
    if user:
        print('system is already to use...')
    else:
        time.sleep(1)
        print('Roles created in progress')
        role1= RoleInfo(id=101,name='Admin')
        role2= RoleInfo(id=102,name='Guest')

        db.session.add_all([role1,role2])
        db.session.commit()
        time.sleep(2)
        print('roles created into system')

        time.sleep(2)
        user=Userinfo(id=99,first_name='suraj',last_name= 'kashid',gender='M',email='suraj@gmail.com',mobile= 6546464164)
        user.roleId= role1.id
        db.session.add(user)
        db.session.commit()
        print('user created into system ')
# same like a user info ---> require logging info
        login= LoginInfo(id=771,username='sruaj',password='surajpython')
        login.userid=user.id
        db.session.add(login)
        db.session.commit()

if __name__ == '__main__':
     initialize_system(reset=True)  #here rquier to write reset is true to work reset command.

