from flask import Flask,render_template,request, redirect, url_for
from database import insert_products, get_data, insert_sales, sales_product, profit_product, daily_sales, daily_profit


#create a flask instance

app=Flask(__name__)

@app.route('/home')
def hello():
    return render_template('index.html')

@app.route('/home')
def home():
    return "home page"

@app.route('/products')
def products():
    prods=get_data("products")
    return render_template("products.html",products=prods)

@app.route('/sales')
def sales():
    sale=get_data("sales")
    return render_template('sales.html',sales=sale)


@app.route('/products', methods=['POST'])
def add_products():

        product_name = request.form['product_name']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        stock_quantity = request.form['stock_quantity']
        
        value=product_name, buying_price, selling_price, stock_quantity
        
        insert_products(value)

        return redirect(url_for('products'))        



@app.route('/sales', methods=['GET'])
def sale():
    sales=get_data("sales")
    products=get_data("products")
    return render_template('sales.html',sales=sales,products=products)


@app.route('/make_sales', methods=['GET','POST'])
def make_sales():
       
        pid=request.form['pid']
        quantity=request.form['quantity']
        sale=(pid,quantity)

        insert_sales(sale)
        return redirect(url_for('sale'))


@app.route('/dashboard')
def dashboard():
    sp=sales_product()
    names=[]
    value=[]
    for i in sp:
        names.append(str(i[0]))
        value.append(float(i[1]))

  
    pp=profit_product()
    names=[]
    profit=[]
    for i in pp:

        names.append(str(i[0]))
        profit.append(float(i[1]))

        
    #sales per day on a line chart 

    ds=daily_sales()
    day=[]
    sl=[]

    for i in ds:
        day.append(str(i[0]))
        sl.append(float(i[1]))

    dp=daily_profit()
    day=[]
    profit=[]

    for i in dp:
        day.append(str(i[0]))
        profit.append(float(i[1]))

    return render_template('dashboard.html',names=names,value=value, profit=profit, day=day,sl=sl)
 




app.run(debug=True)