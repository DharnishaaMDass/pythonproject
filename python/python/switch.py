
#python as a programming language
#flask - web framework
#thonny - IDE
#MVC - model, view, controller

# --- Flask with dynamic variable ---#

# import the Flask class from the flask library

import sqlite3 as sql


from med import *
#from user_authentication import *
from flask import Flask,render_template,request,redirect,jsonify

# create the application object
app = Flask(__name__)


@app.route('/list_customer')
def list_customers():
    rows=list_customer()
    return render_template('list_customer.html', rows=rows)

@app.route('/list_orders')
def list_orders():
    rows=list_order()
    return render_template('list_orders.html', rows=rows)
 
 
@app.route('/list_products')
def list_products():
    rows=list_product()
    return render_template('list_products.html', rows=rows)

@app.route('/list_deliverys')
def list_deliverys():
    rows=list_delivery()
    return render_template('list_deliverys.html', rows=rows)

@app.route('/delete/<Order_Id>')
def delete(Order_Id):  
     delete_orders(Order_Id)
     return redirect('/list_orders')
    

   
@app.route('/find_deliverys',methods=['GET','POST'])
def find():
    if request.method=="POST":
        order_id=request.form['delivery_id']
        row=find_deliverys(delivery_id)
        return render_template('form3.html',row=row)
    else:   
        return render_template('form4.html')
    
@app.route('/new')
def new():
    # Make and blank array of five elements
    row=['']*8
    status='0'
    return render_template('calculationform.html',row=row,status=status)

@app.route('/update',methods=['GET','POST'])
def insert_update():
    Order_Id = request.form['Order_Id']
    Cust_Id = request.form['Cust_Id']
    Product_Id = request.form['Product_Id']
    Order_Quantity = request.form['Order_Quantity']
    Order_Price = request.form['Order_Price']
    Order_Discount = request.form['Order_Discount']
    Order_Date = request.form['Order_Date']
    Order_Total = request.form['Order_Total']

             
    if request.method=='POST' and request.form['status']=='0':
          
        insert_order(Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total)
        return redirect('/list_orders')
          
          
    if request.method=="POST" and request.form['status']=='1':
        update_order(Order_Id,Cust_Id, Product_Id, Order_Quantity,Order_Price,Order_Discount,Order_Date,Order_Total)
        return redirect('/list_orders')
    
    
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('loginnew2.html')
    else:
        return render_template('home2.html')
 
@app.route('/login', methods=['POST'])
def dologin():
    if checklogin(request.form['Cust_Id'],request.form['Cust_Password']):
        session['logged_in'] = True
        return render_template('home2.html')
    else:
        flash('wrong password!')
        return render_template('loginnew2.html',message='Invalid Customer Id or Password!')
        # return redirect('/')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


@app.route('/edit/<delivery_id>')
def edit(delivery_id): 
    row=find_deliverys(delivery_id)
    status='1'
    return render_template('you.html',row=row,status=status)   
    
  

# start the server using the run() method
if __name__ == "__main__":
     app.secret_key = "!mzo53678912489"
     app.run(debug=True,host='0.0.0.0', port=5000)
     
         
     
