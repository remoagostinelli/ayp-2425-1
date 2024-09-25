n = int(input('Número: '))
i = 1
divisores = 0

while i < n:
    if n % i == 0:
        divisores += i
    i += 1

if divisores == n:
    print('Perfecto')
else:
    print('No perfecto')