class Personal:
    def __init__(self, nombre: str, id: int, tipo: str, horas: int):
        self.nombre = nombre
        self.id = id
        self.tipo = tipo
        self.horas = horas
    
    def cobrar(self):
        if self.tipo == 'supersonico':
            monto = self.horas * 60
        elif self.tipo == 'carbon':
            monto = self.horas * 30
        if self.horas > 8:
            monto += 0.3 * monto
        return monto
