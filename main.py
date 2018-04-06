# Importar modulos a ocupar
import buscar as bc

# Selección de operación a ejecutar
print("""Selección acción a ejecutar
	1.Ver las palabras claves
	2.Ver contenido de las palabras claves""")
num = int(input())

# Ejecución de acción a tomar
if num == 1:
	print(bc.claves())
elif num ==2:
	# Busqueda de contendio de la clave
	print('Ingrese palabra clave a buscar: ')
	valor = bc.busqueda(input())
	print('Es una: ',valor)
else:
	print('No ingreso ningun opción valida')
