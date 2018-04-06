# Base de datos del programa
d = {	'Tensorflow'	   	 :'Libreria de machine learning',
		'tf'		 :'Abrevicación de tensorflow',
	'Eager_execution'	 :'Entorno de programación para operaciones rapidas, sin realización de graficas'
    }

# Función de busqueda de frase
def busqueda(frase):

	if frase in d:
		val = d[frase]
	else:
		val = 'La frase ingresada no existe'
	return val

#Función para visualizar las claves
def claves():
	val = d.keys()
	return val



