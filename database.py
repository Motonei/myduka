import psycopg2 
# establish a variable for connection to a postgres db
# psycopg2.connect()=a function used to establish a new connection to postgres db it takes some arguments;1.host-On what server is my database connected 'localhost'=My own device,it is locally hosted in my device
# port-where in my device is the postgress services running;postgres runs on port 5432 by default
# user- username attached to a postgres user.user='postgres'
# password-attached to a postgres user for login
# dbname=The database you intend to use

# cursor=a tool for performing database operations;
# cur .execute() Perform execution
# cur.fetchall()=Afunction used to retrive data from progrss to python
# data format=A list of tuples
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



