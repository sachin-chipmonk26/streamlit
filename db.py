import psycopg2 as db

# hostname = 'localhost'
# database =  'pizzabot'
# username = 'postgres'
# password = '12345'
# port_id = 5432
conn = None
cur = None
try:
    conn = db.connect(host='localhost', dbname='pizzabot', user='postgres', password='12345')
    cur = conn.cursor()
    CREATE_SCRIPT = '''CREATE TABLE IF NOT EXISTS OrderDetails( user_name VARCHAR(20) ,
    address VARCHAR(100),
    phone bigint,
    "orderID" VARCHAR PRIMARY KEY,
    category VARCHAR,
    type VARCHAR,
    is_customized boolean DEFAULT false,
    customization_type VARCHAR,
    crust_type VARCHAR,
    size VARCHAR,
    toppings VARCHAR,
    extra_cheese BOOLEAN,
    quantity INT,
    price FLOAT,
    order_status VARCHAR
)
''' 
    insert_script = '''INSERT INTO public.orderdetails(user_name, address, phone, "orderID", category, type, is_customized, customization_type, crust_type, size, toppings, extra_cheese, quantity, price, order_status) 
        VALUES (%(user_name)s, %(address)s, %(phone)s, %(orderID)s, %(category)s, %(type)s,
        %(is_customized)s, %(customization_type)s, %(crust_type)s, %(size)s,
        %(toppings)s, %(extra_cheese)s, %(quantity)s, %(price)s, %(order_status)s
    )'''
    insert_values = {
    'user_name': 'John',
    'address': '123 Main St',
    'phone': 1234567890,
    'orderID': 'ABC1234567890',
    'category': 'Veg',
    'type': 'Veg Extravaganza',
    'is_customized': False,
    'customization_type': 'Toppings',
    'crust_type' : 'Classic Hand Tossed',
    'size' : 'Medium',
    'toppings': 'Black Olive',
    'extra_cheese': False,
    'quantity': 2,
    'price': 19.99,
    'order_status' : 'Placed',
}

    cur.execute(CREATE_SCRIPT)
    cur.execute(insert_script,insert_values)
    conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
     cur.close()
    if conn is not None:
     conn.close()