import typing

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminante = ((b ** 2 - 4 * a * c) ** 0.5).real

x1 = -b + discriminante / 2 * a
x2 = -b - discriminante / 2 * a

if discriminante > 0:
	print(f"X1 es igual a {x1}")
	print(f"X2 es igual a {x2}")
elif discriminante == 0:
	print(f"X es igual a {x1}")
else:
	print("No hay solución.")