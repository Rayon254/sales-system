import psycopg2

#connect to database 

conn=psycopg2.connect(
    user="postgres",
    dbname="myduka",
    password="1234",
    port=5432,
    host='localhost'
)

curr=conn.cursor()  # used to perform data operations i.e select, update

def get_products():
    curr.execute("select * from products;")
    prods=curr.fetchall()
    for prod in prods :   
        print(prod)

get_products()

#write a function to get sales

def calc_sales():
    curr.execute("select * FROM sales")
    sales=curr.fetchall()
    for sale in sales:
        print(sale)

calc_sales()

def get_data(table_name):
    select=f"select * from {table_name};"
    curr.execute(select)  # contains the sql querry you want to run
    data=curr.fetchall()
    return(data)
        



# insert data

def insert_products(values):
    insert="insert into products(name,buying_price,\
        selling_price,stock_quantity)values(%s,%s,%s,%s);"
    curr.execute(insert,values)
    conn.commit()

product_value=("tilapia",200,500,8)
insert_products(product_value)
get_data('sales')
get_data('products')

# insert sales