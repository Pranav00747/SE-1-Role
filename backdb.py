import mysql.connector

def get_menus():
  conn = mysql.connector.connect(localhost="68.88.12.66", username="perploc", password="petpprn", database="petp")
  cur = conn.cursor()
  cur.execute('SELECT * FROM menus')
  m_dat = cur.fetchall()
  return m_dat

def get_orders():
   conn = mysql.connector.connect(localhost="68.88.12.66", username="perploc", password="petpprn", database="petp")
  cur = conn.cursor()
  cur.execute('SELECT * FROM orders')
  m_dat = cur.fetchall()
  return m_dat
 