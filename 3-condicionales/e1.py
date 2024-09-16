import typing

x = float(input("Dame un número: "))
paridad = 'impar'
signo = 'negativo'

if x % 2 == 0:
	paridad = 'par'

if x > 0:
	signo = 'positivo'

print(f'El número: {x} es {paridad} y {signo}.')