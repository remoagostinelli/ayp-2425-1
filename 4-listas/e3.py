import typing

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1 
for i in ['ñ', 'ch', 'll']:
    alphabet.append(i)
print(alphabet)

#2
for i in range(5):
    print(alphabet[i])

# 3
for i in range(1, 6):
    print(alphabet[-i])
