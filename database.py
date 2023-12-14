import psycopg2 as db

def create_connection():
    try:
        conn = db.connect(host='localhost', dbname='pizzabot', user='postgres', password='12345')
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print(f"Error creating database connection: {e}")
        return None, None

def close_connection(conn, cur):
    try:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    except Exception as e:
        print(f"Error closing database connection: {e}")

def create_order_table(cur):
    try:
        CREATE_SCRIPT = '''
        CREATE TABLE IF NOT EXISTS OrderDetails(
            user_name VARCHAR(20),
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
        cur.execute(CREATE_SCRIPT)
    except Exception as e:
        print(f"Error creating OrderDetails table: {e}")

def insert_order_to_database(cur, order_data):
    try:
        insert_script = '''
        INSERT INTO public.orderdetails(user_name, address, phone, "orderID", category, type, is_customized, customization_type, crust_type, size, toppings, extra_cheese, quantity, price, order_status) 
        VALUES (%(user_name)s, %(address)s, %(phone)s, %(orderID)s, %(category)s, %(type)s,
        %(is_customized)s, %(customization_type)s, %(crust_type)s, %(size)s,
        %(toppings)s, %(extra_cheese)s, %(quantity)s, %(price)s, %(order_status)s)
        '''
        cur.execute(insert_script, order_data)
    except Exception as e:
        print(f"Error inserting order to database: {e}")
