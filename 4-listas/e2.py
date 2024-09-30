import typing

u = [0,0,0]
v = [0,0,0]

print('vector U')
for i in range(len(u)):
    pos = int(input('Número: '))
    u[i] = pos
print('vector V')
for i in range(len(v)):
    pos = int(input('Número: '))
    v[i] = pos

# Suma
suma = []
for i in range(len(u)):
    suma.append(u[i] + v[i])
print(f'U + V = {suma}')

# Producto punto
punto = 0
for i in range(len(u)):
    punto += u[i] * v[i]
print(f'U * V = {punto}')

# Producto cruz
cruz = []
cruz.append(u[1] * v[2] - u[2] * v[1])
cruz.append(u[2] * v[0] - u[0] * v[2])
cruz.append(u[0] * v[1] - u[1] * v[0])
print(f'U x V = {cruz}')
