import sqlite3
from venv import create
import database.accessor

def create_products_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS products(
			id TEXT,
			name TEXT,
			manufacturer TEXT,
			style TEXT,
			purchase_price REAL,
			quantity INTEGER,
			commission_pct INTEGER,

			PRIMARY KEY(id)
	)""")

def create_salespersons_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS salespersons(
			id TEXT,		
			first_name TEXT,
			last_name TEXT,
			address TEXT,
			phone INTEGER,
			start_date TEXT,
			termination_date TEXT,

			PRIMARY KEY(id)
	)""")

def create_managers_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS managers(
			id TEXT,
			first_name TEXT,
			last_name TEXT,

			PRIMARY KEY(id)
	)""")

def create_customers_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
			id TEXT,
			first_name TEXT,
			last_name TEXT,
			address TEXT,
			phone INTEGER,
			start_date TEXT,

			PRIMARY KEY(id)
	)""")

def create_sales_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS sales(
			id TEXT,
			product_id TEXT,
			sales_date TEXT,

			PRIMARY KEY(id)
	)""")

def create_discounts_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS discounts(
			id TEXT,
			product_id TEXT,
			begin_date TEXT,
			end_date TEXT,
			discount_pct INTEGER,

			PRIMARY KEY(id)
	)""")

def create_manager_salespersons_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS manager_salespersons(
			manager_id TEXT,
			salesperson_id TEXT,

			PRIMARY KEY(manager_id, salesperson_id),
			FOREIGN KEY(manager_id) REFERENCES managers(id),
			FOREIGN KEY(salesperson_id) REFERENCES salespersons(id)
	)""")

def create_salesperson_customers_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS salesperson_customers(
			salesperson_id TEXT,
			customer_id TEXT,

			PRIMARY KEY(salesperson_id, customer_id),
			FOREIGN KEY(salesperson_id) REFERENCES salespersons(id),
			FOREIGN KEY(customer_id) REFERENCES customers(id)
	)""")

def create_customer_sales_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS customer_sales(
			customer_id TEXT,
			sale_id TEXT,

			PRIMARY KEY(customer_id, sale_id),
			FOREIGN KEY(customer_id) REFERENCES customers(id),
			FOREIGN KEY(sale_id) REFERENCES sales(id)
	)""")

def create_salesperson_sales_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS salesperson_sales(
			salesperson_id TEXT,
			sale_id TEXT,

			PRIMARY KEY(salesperson_id, sale_id),
			FOREIGN KEY(salesperson_id) REFERENCES salespersons(id),
			FOREIGN KEY(sale_id) REFERENCES sales(id)
	)""")

def create_product_sales_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS product_sales(
			product_id TEXT,
			sale_id TEXT,

			PRIMARY KEY(product_id, sale_id),
			FOREIGN KEY(product_id) REFERENCES products(id),
			FOREIGN KEY(sale_id) REFERENCES sales(id)
	)""")

def create_discount_products_table(cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS discount_products(
			discount_id TEXT,
			product_id TEXT,

			PRIMARY KEY(discount_id, product_id),
			FOREIGN KEY(discount_id) REFERENCES discounts(id),
			FOREIGN KEY(product_id) REFERENCES products(id)
	)""")

def create_all_table(cursor):
	create_products_table(cursor)
	create_salespersons_table(cursor)
	create_managers_table(cursor)
	create_customers_table(cursor)
	create_sales_table(cursor)
	create_discounts_table(cursor)

	create_manager_salespersons_table(cursor)
	create_salesperson_customers_table(cursor)
	create_customer_sales_table(cursor)
	create_salesperson_sales_table(cursor)
	create_product_sales_table(cursor)
	create_discount_products_table(cursor)


def drop_all_tables(cursor):
	cursor.execute("DROP TABLE IF EXISTS products")
	cursor.execute("DROP TABLE IF EXISTS salespersons")
	cursor.execute("DROP TABLE IF EXISTS customers")
	cursor.execute("DROP TABLE IF EXISTS sales")
	cursor.execute("DROP TABLE IF EXISTS discounts")
	cursor.execute("DROP TABLE IF EXISTS managers")

	cursor.execute("DROP TABLE IF EXISTS manager_salespersons")
	cursor.execute("DROP TABLE IF EXISTS salesperon_customers")
	cursor.execute("DROP TABLE IF EXISTS customer_sales")
	cursor.execute("DROP TABLE IF EXISTS salesperson_sales")
	cursor.execute("DROP TABLE IF EXISTS product_sales")
	cursor.execute("DROP TABLE IF EXISTS discount_products")

if __name__ == "__main__":
	conn = sqlite3.connect('bespoked.db')
	conn.row_factory = sqlite3.Row
	cursor = conn.cursor()

	create_all_table(cursor)
	# drop_all_tables(cursor)

	conn.commit()
	cursor.close()
	conn.close()
	