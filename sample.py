from os import access
import database.accessor
import sqlite3
import uuid
from datetime import datetime

conn = sqlite3.connect('bespoked.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# PRODUCT SAMPLE
# -------------------------------------------------------------------
database.accessor.insert_product(cursor, str(
    uuid.uuid4()), 'Verve', 'Trek Bikes', 'Electric', 3300.00, 15, 10)
database.accessor.insert_product(cursor, str(
    uuid.uuid4()), 'Slash', 'Trek Bikes', 'Trail', 12549.99, 5, 15)
database.accessor.insert_product(cursor, str(
    uuid.uuid4()), 'Propel Advanced', 'Giant Bicycle', 'Racing', 5200.00, 15, 10)
database.accessor.insert_product(cursor, str(
    uuid.uuid4()), 'Defy Advanced', 'Giant Bicycle', 'Endurance', 6300.00, 10, 10)
database.accessor.insert_product(cursor, str(
    uuid.uuid4()), 'RL 275', 'Redline', 'Big', 850.00, 20, 8)
database.accessor.insert_product(cursor, str(
    uuid.uuid4()), 'Asset 24', 'Redline', 'Freestyle', 575.00, 40, 10)

# SALESPERSON SAMPLE
# -------------------------------------------------------------------
database.accessor.insert_salesperson(cursor, str(uuid.uuid4(
)), 'Jennifer', 'Henry', '2438 Beechwood Avenue Newark, NJ 07102', 9088660425, '04/12/2022', '06/12/2022')
database.accessor.insert_salesperson(cursor, str(uuid.uuid4(
)), 'Lori', 'Holmes', '4653 Lynn Street Cambridge, MA 02141', 6172796409, '04/28/2018', '09/19/2022')
database.accessor.insert_salesperson(cursor, str(uuid.uuid4()), 'Daniel', 'McCraken',
                                     '316 Terra Cotta Street Thief River Falls, MN 56701', 2186830606, '12/28/2019', '07/01/2022')

# MANAGER SAMPLE
# -------------------------------------------------------------------
database.accessor.insert_manager(cursor, str(uuid.uuid4()), "Raymond", "Dix")
database.accessor.insert_manager(cursor, str(uuid.uuid4()), "Erin", "Howell")

# MANAGER SALESPERSONS SAMPLE
# -------------------------------------------------------------------
database.accessor.insert_manager_salespersons(
    cursor, 'e4d3f660-5d40-4c1d-a58e-151cfcc55a2e', 'Raymond Dix')
database.accessor.insert_manager_salespersons(
    cursor, 'a3c2d1b5-a772-4602-9eb7-2b997528c23f', 'Raymond Dix')
database.accessor.insert_manager_salespersons(
    cursor, 'edef7d4c-9055-42ca-bb7c-2bc55d815b4e', 'Erin Howell')

# PRINTS
# -------------------------------------------------------------------
products = database.accessor.get_products(cursor)
managers = database.accessor.get_managers(cursor)
salespersons = database.accessor.get_salespersons(cursor)
salesperson_managers = database.accessor.get_manager_salespersons(cursor)

print("products")
for product in products:
    print(product['name'])

print("managers")
for manager in managers:
    print([manager['id'], manager['first_name'], manager['last_name']])

print("salesperons")
for salesperson in salespersons:
    print([salesperson['id'], salesperson['first_name'], salesperson['last_name']])

print("manager_salespersons")
for row in salesperson_managers:
    print([row["manager_id"], row["salesperson_id"]])

conn.commit()
cursor.close()
conn.close()
