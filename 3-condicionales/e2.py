import typing

nombre = input('Nombre: ')
edad = int(input('Edad: '))

if edad > 0:
	if edad <= 4:
		precio_entrada = 0	
	elif edad > 4 and edad <= 18:
		precio_entrada = 1.5
	elif edad >= 60:
		precio_entrada = 1
	else:
		precio_entrada = 2
	print(f'El cliente {nombre} tiene: {edad} años y su entrada de cine cuesta: ${precio_entrada}.')
else:
	print('Error.')
