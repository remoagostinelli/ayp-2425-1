n = input('Número: ')
cifras = len(n)
i = -1
cifras_volteadas = []
volteado = ''

while i >= - cifras:
    cifras_volteadas.append(n[i])
    i -= 1

for i in cifras_volteadas:
    volteado += i

print(volteado)