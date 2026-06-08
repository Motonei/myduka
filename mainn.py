import psycopg2 

conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='Abigael#33',dbname='myduka')
cur=conn.cursor()
def fetch_products():
     cur.execute("select * from products")
     products_data=cur.fetchall()
     return products_data

def insert_into(values):
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)",values)
    conn.commit()
product1=('book',1200,1300,25)
insert_into(product1)

def sales_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date,
               SUM(sales.quantity * products.selling_price) AS total_sales
        FROM sales
        JOIN products ON products.id = sales.pid
        GROUP BY sale_date
    """)
    return cur.fetchall()


def profit_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date,
               SUM(sales.quantity * (products.selling_price - products.buying_price)) AS total_profit
        FROM sales
        JOIN products ON products.id = sales.pid
        GROUP BY sale_date
    """)
    return cur.fetchall()


print("SALES:", sales_per_day())
print("PROFIT:", profit_per_day())


def sales_per_product():
    cur.execute("""
        select products.name as p_name,
               sum(sales.quantity * products.selling_price) as total_sales
        from products
        join sales on sales.pid = products.id
        group by p_name;
    """)
    product_sales = cur.fetchall()
    return product_sales

def profit_per_product():
    cur.execute("""
        select products.name as p_name,
               sum(
                   sales.quantity *
                   (products.selling_price - products.buying_price)
               ) as total_sales
        from products
        join sales on sales.pid = products.id
        group by p_name;
    """)
    product_profit = cur.fetchall()
    return product_profit 