suma = 0

while True:
    n = int(input('Número: '))
    if n < 0:
        break
    suma += n

print(f'Total: {suma}')