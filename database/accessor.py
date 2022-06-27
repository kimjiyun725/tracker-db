# PRODUCT FUNCTIONS
def insert_product(cursor, id_, name, manufacturer, style, purchase_price, quantity, commission_pct):
    try:
        product_rows = cursor.execute(
            """
            INSERT INTO products
            (id, name, manufacturer, style, purchase_price, quantity, commission_pct)
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,
            (id_, name, manufacturer, style,
             purchase_price, quantity, commission_pct)
        )

        if not product_rows.lastrowid:
            return False

        return True
    except:
        return False


def get_products(cursor):
    try:
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return {}

# SALESPERSON FUNCTIONS


def insert_salesperson(cursor, id_, first_name, last_name, address, phone, start_date, termination_date):
    try:
        salesperson_rows = cursor.execute(
            """
            INSERT INTO salespersons
            (id, first_name, last_name, address, phone, start_date, termination_date)
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,
            (id_, first_name, last_name, address,
             phone, start_date, termination_date)
        )

        if not salesperson_rows.lastrowid:
            return False

        return True
    except:
        return False


def get_salespersons(cursor):
    try:
        cursor.execute("SELECT * FROM salespersons")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return {}

# MANAGER FUNCTIONS


def insert_manager(cursor, id_, first_name, last_name):
    try:
        manager_rows = cursor.execute(
            """
            INSERT INTO managers
            (id, first_name, last_name)
            VALUES(?, ?, ?)
            """,
            (id_, first_name, last_name)
        )

        if not manager_rows.lastrowid:
            return False

        return True
    except:
        return False


def get_managers(cursor):
    try:
        cursor.execute("SELECT * FROM managers")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return {}

# CROSS REFERENCE FUNCTIONS


def insert_manager_salespersons(cursor, salesperson_id, manager_checker):
    list_of_managers = get_managers(cursor)
    # desired_manager_id = ''
    for manager in list_of_managers:
        manager_fullname = manager['first_name'] + " " + manager['last_name']
        if manager_checker == manager_fullname:
            # desired_manager_id = manager['id']

            try:
                manager_salespersons_rows = cursor.execute(
                    """
                    INSERT INTO manager_salespersons
                    (manager_id, salesperson_id)
                    VALUES(?, ?)
                    """,
                    (manager['id'], salesperson_id)
                )
                if not manager_salespersons_rows.lastrowid:
                    return False

                return True
            except:
                return False

    return False


def get_manager_salespersons(cursor):
    try:
        cursor.execute("SELECT * FROM manager_salespersons")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return {}
