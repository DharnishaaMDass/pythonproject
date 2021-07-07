import sqlite3 as sql

from functools import wraps
from flask import session,flash,redirect,url_for

connect_db ='smp3.db'


def list_customer():
  with sql.connect(connect_db) as db:
    qry = 'select * from customer' 
    result=db.execute(qry)
    return(result)

def list_order():
  with sql.connect(connect_db) as db:
    qry = 'select * from orders' 
    result=db.execute(qry)
    return(result)



def list_product():
  with sql.connect(connect_db) as db:
    qry = 'select * from products' 
    result=db.execute(qry)
    return(result)


def list_delivery():
  with sql.connect(connect_db) as db:
    qry = 'select * from deliverys' 
    result=db.execute(qry)
    return(result)

def result():
  rows=list_order()
  rows=list_product()
  rows=list_delivery()
  for row in rows:
    print (row)
    
def find_deliverys(deliverys_id):
  with sql.connect(connect_db) as db:
    qry = 'select * from deliverys where delivery_id=?'
    result=db.execute(qry,(delivery_id,)).fetchone()
    return(result)

    
def delete_orders(Order_Id):
  with sql.connect(connect_db) as db:
    qry='delete from orders where Order_Id=?' 
    db.execute(qry,(Order_Id,))
    
 
def insert_delivery(delivery_id,delivery_address,receive_status):
  with sql.connect(connect_db) as db:
    qry='insert into deliverys (delivery_id,delivery_address,receive_status) values (?,?,?)' 
    db.execute(qry,(delivery_id,delivery_address,receive_status))
    
def insert_order(Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total):
  with sql.connect(connect_db) as db:
    qry='insert into orders (Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total) values (?,?,?,?,?,?,?,?)' 
    db.execute(qry,(Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total))
    

def update_order(Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total):
  with sql.connect(connect_db) as db:
    qry='update order set Order_Id=?, Cust_Id=?, Product_Id=?, Order_Quantity=?,Order_Price=?,Order_Discount=?,Order_Date=?,Order_Total=? where Order_Id=?'
    db.execute(qry, (Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total))
  with sql.connect(connect_db) as db:
    qry='insert into order (Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total) values (?,?,?,?,?,?,?,?)' 
    db.execute(qry,(Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total))
    
    
def check_Order_Id(Order_Id):
  with sql.connect(connect_db) as db: 
    qry = 'select Order_Id,Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total from orders where Order_Id=?'
    result=db.execute(qry,(Order_Id,)).fetchone()
    return(result)
    

def checklogin(Cust_Id,Cust_Password):
  with sql.connect(connect_db) as db: 
    qry = 'select Cust_Id,Cust_Password from customer where Cust_Id=? and Cust_Password=?'
    result=db.execute(qry,(Cust_Id,Cust_Password)).fetchone()
    return(result)
"""  
def update_delivery(delivery_id,delivery_address,receive_status):
  with sql.connect(connect_db) as db:
    qry='update deliverys set receive_status=?,delivery_address=?, where delivery_id=?'
    db.execute(qry, (delivery_id,delivery_address,receive_status))
  with sql.connect(connect_db) as db:
    qry='insert into deliverys (delivery_id,delivery_address,receive_status) values (?,?,?)' 
    db.execute(qry,(delivery_id,delivery_address,receive_status))
"""  

# helper function

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
        return f(*args, **kwargs)
    else:
        flash("You need to login first")
        return redirect(url_for('home'))
  return wrap