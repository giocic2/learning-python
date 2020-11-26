def sayHi(username):
	"""
	Stampa a schermo un messaggio di benvenuto personalizzato.
	Poi fornisce informazioni circa lo script e l'autore.
	"""
	if username==None:
		print('Hello World!')
	else:
		print("Hello "+username+"!")
	print('This script was created on 22 september 2020.')
	print('The author name is Giordano Cicioni.')
	return None

sayHi(None)
# 'sayHi()' non ammesso, perché l'argomento 'username' è obbligatorio.
"""
'sayHi()' non ammesso, perché l'argomento 'username' è obbligatorio.
"""
saluta = sayHi
print('Ora verrà rieseguita la stessa funzione, ma avendole riassegnato il nome (da \'sayHi\' a \'saluta\').')
saluta(None)

def sayBye(username):
	"""
	Stampa a schermo un messaggio di arrivederci personalizzato.
	"""
	if username==None:
		print("Bye World!")
	else:
		print("Bye "+username+"!")
	#'return' si può ommettere quando il valore è 'None'.

def saySomething(hiOrBye, username):
	"""
	E' una funzione del tutto superflua, giusto per far vedere che si può passare una fuzione come argomento.
	"""
	hiOrBye(username)

myName="giocic2"
saySomething(sayBye,myName)
