class Carro():
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0

    def abastecer(self, quantidade: float):
        self.qtd_de_combustivel += quantidade

# aqui vc coloca o código principal
if __name__ == '__main__': 
    my_car = Carro()
    
    my_car.marca = 'Toyota'
    my_car.modelo = 'Corolla'
    my_car.placa = 'RRO4E26'
    my_car.abastecer(10)
    my_car.abastecer(4)
    print(my_car.marca)
    print(my_car.qtd_de_combustivel)
