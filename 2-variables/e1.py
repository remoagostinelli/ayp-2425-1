import typing

volumen_reservorio: float = 4.445e8
lluvia: float = 5e6

# 1
lluvia = lluvia * 0.9

# 2
volumen_reservorio += lluvia

# 3
volumen_reservorio = volumen_reservorio * 1.05

# 4
volumen_reservorio = volumen_reservorio * 0.98

# 5
volumen_reservorio -= 2.5e5

# 6
print(volumen_reservorio)