import psycopg2 as db

def create_table():
    conn = None
    try:
        conn = db.connect(host='localhost', dbname='pizzabot', user='postgres', password='12345')
        cur = conn.cursor()

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
        conn.commit()

    except Exception as error:
        print(f"Error creating table: {error}")
    finally:
        if conn is not None:
            conn.close()

def insert_order(order_values):
    conn = None
    try:
        conn = db.connect(host='localhost', dbname='pizzabot', user='postgres', password='12345')
        cur = conn.cursor()

        insert_script = '''
        INSERT INTO public.orderdetails(
            user_name, address, phone, "orderID", category, type, is_customized,
            customization_type, crust_type, size, toppings, extra_cheese,
            quantity, price, order_status
        ) VALUES (
            %(user_name)s, %(address)s, %(phone)s, %(orderID)s, %(category)s, %(type)s,
            %(is_customized)s, %(customization_type)s, %(crust_type)s, %(size)s,
            %(toppings)s, %(extra_cheese)s, %(quantity)s, %(price)s, %(order_status)s
        )
        '''

        cur.execute(insert_script, order_values)
        conn.commit()

    except Exception as error:
        print(f"Error inserting order: {error}")
    finally:
        if conn is not None:
            conn.close()
