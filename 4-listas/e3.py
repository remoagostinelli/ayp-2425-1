import typing

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1 
print('#1')
for i in ['ñ', 'ch', 'll']:
    alphabet.append(i)
print(alphabet)
print()

#2
print('#2')
for i in range(5):
    print(alphabet[i])
print()

# 3
print('#3')
for i in range(1, 6):
    print(alphabet[-i])
print()

# 4
print('#4')
for i in range(len(alphabet))[1::2]:
    print(alphabet[i])
print()

# 5
print('#5')
for i in alphabet[::-1]:
    print(i)
print()
