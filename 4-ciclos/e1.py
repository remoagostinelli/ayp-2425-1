n = int(input('Número: '))
i = 2
primo = 1

while i < n:
    if n % i == 0:
        primo = 0
        break
    i += 1

if primo and n != 1:
    print('Primo')
else:
    print('No primo')