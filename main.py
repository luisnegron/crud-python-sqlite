import sqlite3
import os
import functions

# Connect to sqlite database
con = sqlite3.connect('phonebook.db')

try:
	# Cursor object
	cur = con.cursor()
	
	# Execute query
	cur.execute('''CREATE TABLE IF NOT EXISTS Contacts (
    code_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT (100) NOT NULL,
    address TEXT (500) NOT NULL,
    telephone INTEGER NOT NULL);''')
    
	# Commit changes
	con.commit()
    
	# Print successful message
	print('La tabla contactos ha sido creada exitosamente')
	
except:
	print('Un error ha ocurrido...')

	# Roll back if in case of issue
	con.rollback()

#menu for choose options
def menu():
	print ("Selecciona una opción")
	print ("\t1 - Crear nuevo contacto")
	print ("\t2 - Visualizar contactos")
	print ("\t3 - Modificar un contacto")
	print ("\t4 - Borrar un contacto")
	print ("\t5 - salir")

while True:
	menu()
	
	option = input("inserta un numero valor >> ")
	if option=="1":
		functions.insert()
		os.system('clear')		
	elif option=="2":
		functions.retrieve()
	elif option=="3":
		functions.modify()
		os.system('clear')	
	elif option=="4":
		functions.erase()
		os.system('clear')
	elif option=="5":
		break
		os.system('clear')
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
	
# Close connection
con.close()
