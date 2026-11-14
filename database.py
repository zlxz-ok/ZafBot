import sqlite3
from urllib.parse import urlparse

conexion = sqlite3.connect("products.db")
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
	name TEXT,
	link TEXT,
	precio REAL
 )
  """)
cursor.execute("""
 CREATE TABLE IF NOT EXISTS config (
   key TEXT PRIMARY KEY,
   url TEXT NOT NULL
 )
 """)

def addproduct(name,link,precio):
	cursor.execute("""
    INSERT INTO productos (name,link,precio)
	VALUES (?,?,?)
    """,(name,link,precio,))
	conexion.commit()
def deleteproduct(id):
	cursor.execute("""
    DELETE FROM productos WHERE id = ?
    """,(id,))
	if cursor.rowcount == 0:
		return False
	else:
		conexion.commit()
		return True  
def webhookchange(newwebhook):
	parse = urlparse(newwebhook)
	if not (parse.scheme == "https" and parse.path.startswith("/api/webhooks/")):
		return False, "La URL de la webhook no tiene un formato válido"
	else:	
		cursor.execute("""
   	    INSERT INTO config (key,url)
		VALUES (?,?)
		ON CONFLICT(key) DO UPDATE SET url = excluded.url
	    """,("webhook",newwebhook))
		conexion.commit()
		return True, "Webhook cambiada correctamente"
def view():
	cursor.execute("""
    SELECT * FROM productos
    """)
	viewall = cursor.fetchall()
	return viewall
def get():
	conexion = sqlite3.connect("products.db")
	cursor = conexion.cursor()
	cursor.execute("""
    SELECT * FROM productos
    """)
	viewall = cursor.fetchall()
	productos = []
	for id,name,link,precio in viewall:	
		datos = {
			"id": id,
			"name": name,
			"link": link,
			"precio": precio
        }
		productos.append(datos)
	return productos
def editprice(newprice,id):
	cursor.execute("""
    UPDATE productos SET precio = ? WHERE id = ?
    """,(newprice,id,))
	if cursor.rowcount == 0:
		return False
	else:
		conexion.commit()
		return True 
def createcursor():
	conexion = sqlite3.connect("products.db")
	return conexion