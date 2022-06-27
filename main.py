from flask import Flask, jsonify, request
import json
import database.accessor
import sqlite3
import uuid

app = Flask(__name__)

# PRODUCTS API ROUTES


@app.route('/products', methods=['GET', 'POST'])
def products():
    global id_
    global name_
    global manufacturer
    global style
    global purchase_price
    global quantity
    global commission_pct

    if request.method == 'POST':
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        id_ = request_data['id']
        name_ = request_data['name']
        manufacturer = request_data['manufacturer']
        style = request_data['style']
        purchase_price = request_data['purchase_price']
        quantity = request_data['quantity']
        commission_pct = request_data['commission_pct']

        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        success = database.accessor.insert_product(
            cursor, id_, name_, manufacturer, style, purchase_price, quantity, commission_pct)
        print(f"{success}")

        conn.commit()
        cursor.close()
        conn.close()

        return " "

    elif request.method == 'GET':
        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        rows = database.accessor.get_products(cursor)
        list_of_products = []
        for row in rows:
            list_of_products.append(
                {
                    "id": row["id"],
                    "name": row["name"],
                    "manufacturer": row["manufacturer"],
                    "style": row["style"],
                    "purchase_price": row["purchase_price"],
                    "quantity": row["quantity"],
                    "commission_pct": row["commission_pct"]
                }
            )

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(list_of_products)

    return " "

# SALESPERSONS API ROUTES


@app.route('/salespersons', methods=['GET', 'POST'])
def salespersons():
    global id_
    global first_name
    global last_name
    global address
    global phone
    global start_date
    global termination_date
    global manager

    if request.method == 'POST':
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        id_ = request_data['id']
        first_name = request_data['first_name']
        last_name = request_data['last_name']
        address = request_data['address']
        phone = request_data['phone']
        start_date = request_data['start_date']
        termination_date = request_data['termination_date']
        manager = request_data['manager']

        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        checking = database.accessor.insert_manager_salespersons(
            cursor, id_, manager)
        if checking == False:
            conn.commit()
            cursor.close()
            conn.close()
            return " "

        success = database.accessor.insert_salesperson(
            cursor, id_, first_name, last_name, address, phone, start_date, termination_date)
        print(f"{success}")

        conn.commit()
        cursor.close()
        conn.close()

        return " "

    elif request.method == 'GET':
        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        manager_salespersons = database.accessor.get_manager_salespersons(
            cursor)
        managers = database.accessor.get_managers(cursor)
        salespersons = database.accessor.get_salespersons(cursor)

        list_of_salespersons = []
        for id_ in manager_salespersons:
            for salesperson in salespersons:
                if id_['salesperson_id'] == salesperson['id']:
                    desired_manager = ''
                    for manager in managers:
                        if id_['manager_id'] == manager['id']:
                            desired_manager = manager['first_name'] + \
                                " " + manager['last_name']

                    list_of_salespersons.append(
                        {
                            "id": salesperson["id"],
                            "first_name": salesperson["first_name"],
                            "last_name": salesperson["last_name"],
                            "address": salesperson["address"],
                            "phone": salesperson["phone"],
                            "start_date": salesperson["start_date"],
                            "termination_date": salesperson["termination_date"],
                            "manager": desired_manager
                        }
                    )

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(list_of_salespersons)

# MANAGERS API ROUTE


@app.route('/managers', methods=['GET', 'POST'])
def managers():
    global id_
    global first_name
    global last_name

    if request.method == 'POST':
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        id_ = request_data['id']
        first_name = request_data['first_name']
        last_name = request_data['last_name']

        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        success = database.accessor.insert_manager(
            cursor, id_, first_name, last_name)
        print(f"{success}")

        conn.commit()
        cursor.close()
        conn.close()

        return " "

    elif request.method == 'GET':
        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        rows = database.accessor.get_managers(cursor)
        list_of_managers = []
        for row in rows:
            list_of_managers.append(
                {
                    "id": row["id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                }
            )

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(list_of_managers)

    return " "
