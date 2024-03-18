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

# delete a product

# def delete_product():
#     delete_query = "DELETE FROM products WHERE id = %s;"
#     curr.execute(delete_query, (product_id,))
#     conn.commit()

# delete_product()

#write a function to get sales define a cfunction (def)

def calc_sales():
    curr.execute("select * FROM sales")
    sales=curr.fetchall()
    for sale in sales:
        print(sale)

# calc_sales()

def get_data(table_name):
    select=f"select * from {table_name};"
    curr.execute(select)  # contains the sql querry you want to run   curr=cursor.execute
    data=curr.fetchall()
    return(data)
        


# insert data

def insert_products(values):
    insert="insert into products(name,buying_price,\
        selling_price,stock_quantity)values(%s,%s,%s,%s);"
    curr.execute(insert,values)
    conn.commit()

# items=("tilapia",200,500,8)
# insert_product(items)


# insert sales
def insert_sales(values):
    insert="insert into sales(pid,quantity,created_at)values(%s,%s,now());"

    curr.execute(insert,values)
    conn.commit()

#sales per product
def sales_product():
    display="select name,sum(selling_price*quantity) FROM products join sales on products.id=sales.pid Group by name;"
    curr.execute(display)
    data=curr.fetchall()
    return(data)

# profit per product

def profit_product():
    profit="select name,sum(selling_price-buying_price) FROM products Group by name;"
    curr.execute(profit)
    data=curr.fetchall()
    return(data)

# sales per day

def daily_sales():
    dailysales="select date(sales.created_at) as day,sum(selling_price*quantity) FROM products join sales on products.id=sales.pid Group by day Order by day;"
    curr.execute(dailysales)
    data=curr.fetchall()
    return(data)

# profit per day

def daily_profit():
    profit="select date(sales.created_at) as day, sum(selling_price-buying_price) FROM products join sales on products.id=sales.pid Group by day Order by day;"
    curr.execute(profit)
    data=curr.fetchall()
    return(data)





