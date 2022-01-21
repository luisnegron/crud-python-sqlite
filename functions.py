import sqlite3

con = sqlite3.connect('phonebook.db')

def insert():
	name = input("ingresar el nombre: ")
	address = input("ingresar la dirección: ")
	telephone = int(input("ingresar el numero telefonico: "))

	data = name,address,telephone

	try:
		cur = con.cursor()
		cur.execute("INSERT INTO contacts(name, address, telephone) VALUES(?,?,?)",data)
		con.commit()
		print ("Se añadio correctamente el nuevo contacto!")

	except:
		print ("error no se agrego el contacto!!!")
		con.rollback()
		
def retrieve():
	try:
		cur = con.cursor()
		cur.execute("SELECT * FROM contacts")
		while True:
			record=cur.fetchone()
			if record==None:
				break
			print (record)

	except:
		print ("error no se encontro información!!!")
		con.rollback()
		
def modify():
	code = int(input("ingresar el id de contacto a modificar: "))
	name = input("ingresar el nombre: ")
	address = input("ingresar la dirección: ")
	telephone = int(input("ingresar el numero telefonico: "))

	data = name,address,telephone,code

	try:
		cur = con.cursor()
		cur.execute("update contacts set name=?,address=?,telephone=? where code_id=?;",data)
		
		con.commit()
		print("Se actualizo correctamente el contacto")

	except:
		print("error al actualizar!!!")
		con.rollback()
	
def erase():
	code = int(input("ingresar el id de contacto a borrar: "))
	
	data = code,

	try:
		cur = con.cursor()
		cur.execute("DELETE from contacts where code_id=?;",data)
		con.commit()
		print("Se borró correctamente el contacto")

	except:
		print("error en el borrado!!!")
		con.rollback()
