import typing

puntos = int(input("Puntos: "))

if puntos >= 51 and puntos <= 150:
	premio = "Bronce"
elif puntos >= 151 and puntos <= 180:
	premio = "Plata"
elif puntos >= 181 and puntos <= 200:
	premio = "Oro"
else:
	premio = "No hay premio"

if premio != "No hay premio":
	print(f"Felicitaciones, Ganaste la medalla de {premio} por haber tenido {puntos} pts!")
else:
	print(premio)