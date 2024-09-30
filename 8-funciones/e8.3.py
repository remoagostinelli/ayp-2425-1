import typing

def registrar(cedula, nombre, apellido, telefono, razon):
  return [cedula, nombre, apellido, telefono, razon]


def main():
  cedula = int(input('Número de cédula: '))
  nombre = input('Nombre: ')
  apellido = input('Apellido: ')
  telefono = int(input('Teléfono: '))
  razon = input('Razón de consulta: ')
  print(registrar(cedula, nombre, apellido, telefono, razon))

main()
