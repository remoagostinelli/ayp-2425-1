print("Considera un triangulo de lados a, b y c.")
print("Introduce el valor de cada lado.")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Herón
s = (a + b + c) / 2
A = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"El área del triángulo es {A}")