import sqlite3


conn = sqlite3.connect('employees.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees 
             (EMPID INTEGER PRIMARY KEY, 
              EMPName TEXT, 
              EMPGender TEXT, 
              EMPPhone TEXT, 
              EMPBdate DATE)''')
conn.commit()
conn.close()
