from typing import List
from personal import Personal

class SamanTrain:
    def __init__(self):
        self.personal: List[Personal] = []

    def register(self):
        nombre = input('Nombre: ')
        cedula = input('Cédula: ')
        while True:
            tipo = input('Tipo de tren: ').lower()
            if tipo != 'supersonico' and tipo != 'carbon':
                print('Tipo de tren inválido. Intente de nuevo.')
            else:
                break
        horas = int(input('Horas de trabajo: '))
        persona = Personal(nombre, cedula, tipo, horas)
        self.personal.append(persona)

    def query(self):
        if len(self.personal) == 0:
            print('''
                    No hay personal registrado.
                    ''')
            return

        #  - La cantidad total de personal con su información
        print(f'''
                Personal: {len(self.personal)}
                ''')
        for i in self.personal:
            print(f'''
                    Nombre: {i.nombre}
                    Cédula: {i.id}
                    Tren: {i.tipo}
                    Horas de trabajo: {i.horas}
                    ''')
    
        # - La cantidad de personal por tipo de tren
        supersonico = 0
        carbon = 0
        for i in self.personal:
            if i.tipo == 'supersonico':
                supersonico += 1
            elif i.tipo == 'carbon':
                carbon += 1
        print(f'''
                Personal por tipo de tren:
                Supersónico: {supersonico}
                Carbón: {carbon}
                ''')
        
        # - La cantidad de personal a quienes se les otorgó el aumento
        count = 0
        for i in self.personal:
            if i.horas > 8:
                count += 1
        print(f'''
                Personal a quienes se les otorgó el aumento: {count}
                ''')

        # - El Promedio de pago por tipo de tren
        avg_supersonico = 0
        avg_carbon = 0
        for i in self.personal:
            if i.tipo == 'supersonico':
                avg_supersonico += i.cobrar()
            elif i.tipo == 'carbon':
                avg_carbon += i.cobrar()
        if supersonico != 0:
            avg_supersonico = avg_supersonico / supersonico
        if carbon != 0:
            avg_carbon = avg_carbon / carbon
        print(f'''
                Promedio de pago:
                Supersónico: {avg_supersonico}
                Carbón: {avg_carbon}
                ''')

    def menu(self):
        while True:
            option = int(input('''
        
        1. Registrar personal
        2. Consultar personal
        3. Salir
                           
        '''))
            if option == 1:
                self.register()
            elif option == 2:
                self.query()
            elif option == 3:
                break
