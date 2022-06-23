from concurrent.futures.process import _python_exit
from ctypes import addressof
from flask import Flask, jsonify, request
import json
import database.accessor
import sqlite3
import uuid

app = Flask(__name__)

# API Routes
@app.route('/products',methods=['GET', 'POST'])
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
        for row in request_data:
            id_ = row['id']
            name_ = row['name']
            manufacturer = row['manufacturer']
            style = row['style']
            purchase_price = row['purchase_price']
            quantity = row['quantity']
            commission_pct = row['commission_pct']

        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        success = database.accessor.insert_product(cursor, id_, name_, manufacturer, style, purchase_price, quantity, commission_pct)

        print(f"{success}")

        rows = database.accessor.get_products(cursor)
        print("Print out input:")
        for row in rows:
            print([row["id"], row["name"], row["manufacturer"], row["style"], row["purchase_price"], row["quantity"], row["commission_pct"]])

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
        print(list_of_products)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(list_of_products)

    return " "

@app.route('/salespersons', methods=['GET','POST'])
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
        for row in request_data:
            id_ = row['id']
            first_name = row['first_name']
            last_name = row['last_name']
            address = row['address']
            phone = row['phone']
            start_date = row['start_date']
            termination_date = row['termination_date']
            manager = row['manager']

        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        checking = database.accessor.check_managers(cursor, manager)
        if checking == False:
            conn.commit()
            cursor.close()
            conn.close()
            return " "

        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        success = database.accessor.insert_salesperson(cursor, id_, first_name, last_name, address, phone, start_date, termination_date)

        print(f"{success}")

        rows = database.accessor.get_salespersons(cursor)
        print("Print out input:")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return " "

    elif request.method == 'GET':
        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        rows = database.accessor.get_salespersons(cursor)
        list_of_salespersons = []
        for row in rows:
            list_of_salespersons.append(
                {
                "id": row["id"], 
                "first_name": row["first_name"], 
                "last_name": row["last_name"], 
                "address": row["address"], 
                "phone": row["phone"], 
                "start_date": row["start_date"], 
                "termination_date": row["termination_date"], 
                }
            )
        print(list_of_salespersons)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(list_of_salespersons)
    
@app.route('/managers', methods=['GET','POST'])
def managers():
    global id_
    global first_name
    global last_name

    if request.method == 'POST':
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        for row in request_data:
            id_ = row['id']
            first_name = row['first_name']
            last_name = row['last_name']

        conn = sqlite3.connect('bespoked.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        success = database.accessor.insert_manager(cursor, id_, first_name, last_name)

        print(f"{success}")

        rows = database.accessor.get_managers(cursor)
        print("Print out input:")
        
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
        print(list_of_managers)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(list_of_managers)

    return " "