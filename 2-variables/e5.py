import typing

k: float = 8.85e-12

q1 = float(input("Carga 1: "))
q2 = float(input("Carga 2: "))
r = float(input("Distancia entre las cargas: "))

f: float = k * ((q1 * q2) / (r ** 2)) * r

print(f"La magnitud de la fuerza es igual a {f}.")