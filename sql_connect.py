import sqlite3
from sqlite3 import Error

#connect to the database
def connect():
	conn = None
	try:
		#connect to the database
		conn = sqlite3.connect("mydb")
	except Error as e:
		print(e)
	return conn

#insert the username into the tables, and make the username as the primary key
def insert_username(info_name):
	#insert statement and values
	sql = """INSERT OR REPLACE INTO User(username, fail_email, fail_shopping, fail_banking, time_email_start, time_email_end, time_shopping_start, time_shopping_end, time_banking_start, time_banking_end, email_password, shopping_password, banking_password) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
	value = (info_name,0,0,0,'','','','','','','','','')
	conn = connect()
	cur = conn.cursor()
	cur.execute(sql, value)
	conn.commit()
	cur.close()
	conn.close()

#insert the assigned password into the tables by using the username
def insert_password(info_name, info_epass, password_type):
	#insert statement and values
	if password_type == "email_password":
		sql = """UPDATE User SET email_password = ?  WHERE username = ?"""
	elif password_type == "shopping_password":
		sql = """UPDATE User SET shopping_password = ?  WHERE username = ?"""
	elif password_type == "banking_password":
		sql = """UPDATE User SET banking_password = ?  WHERE username = ?"""
	
	value = (info_epass, info_name)
	conn = connect()
	cur = conn.cursor()
	cur.execute(sql, value)
	conn.commit()
	cur.close()
	conn.close()

#select the password from the tables by using the username
def get_password(info_name, password_type):
	#insert statement
	if password_type == "email_password":
		sql = """SELECT email_password FROM User WHERE username = ?"""
	elif password_type == "shopping_password":
		sql = """SELECT shopping_password FROM User WHERE username = ?"""
	elif password_type == "banking_password":
		sql = """SELECT banking_password FROM User WHERE username = ?"""
	value = (info_name,)
	conn = connect()
	cur = conn.cursor()
	cur.execute(sql, value)
	ar = [str(r[0]) for r in cur.fetchall()]
	conn.commit()
	cur.close()
	conn.close()
	result = ar[0]
	r = result.split(' ')
	for i in range(0, len(r)):
		if r[i] == '':
			r = r[:i]
	return r

#insert the time of failures into the table by using username
def count_failure(info_name, info_count, password_type):
	#insert statement and values
	if password_type == "email_password":
		sql = """UPDATE User SET fail_email = ?  WHERE username = ?"""
	elif password_type == "shopping_password":
		sql = """UPDATE User SET fail_shopping = ?  WHERE username = ?"""
	elif password_type == "banking_password":
		sql = """UPDATE User SET fail_banking = ?  WHERE username = ?"""
	
	value = (info_count, info_name)
	conn = connect()
	cur = conn.cursor()
	cur.execute(sql, value)
	conn.commit()
	cur.close()
	conn.close()

#insert the time cost into the table by using the username
def count_time(info_name, info_time_start, info_time_end, password_type):
	#insert statement and values
	if password_type == "email_password":
		sql = """UPDATE User SET time_email_start = ?  WHERE username = ?"""
		sql2 = """UPDATE User SET time_email_end = ?  WHERE username = ?"""
	elif password_type == "shopping_password":
		sql = """UPDATE User SET time_shopping_start = ?  WHERE username = ?"""
		sql2 = """UPDATE User SET time_shopping_end = ?  WHERE username = ?"""
	elif password_type == "banking_password":
		sql = """UPDATE User SET time_banking_start = ?  WHERE username = ?"""
		sql2 = """UPDATE User SET time_banking_end = ?  WHERE username = ?"""
	
	value_start = (info_time_start, info_name)
	value_end = (info_time_end, info_name)
	conn = connect()
	cur = conn.cursor()
	cur.execute(sql, value_start)
	cur.execute(sql2, value_end)
	conn.commit()
	cur.close()
	conn.close()
