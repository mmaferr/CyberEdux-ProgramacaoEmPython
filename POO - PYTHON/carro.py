class Carro():
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0

    def abastecer(self, quantidade: float):
        # método de limite 
        if self.qtd_de_combustivel + quantidade > 30:
            print("*** Não é permitido abastecer mais do que 30 litros! ***")
            self.qtd_de_combustivel = 30
        else:
            self.qtd_de_combustivel += quantidade

    def exibir(self):
         print('------------------------------------------------\n                      MENU \n------------------------------------------------\n* Marca: ', my_car.marca)
         print('* MODELO: ', self.modelo)
         print('* PLACA: ', self.placa)
         print('* QUANTIDADE DE COMBUSTÍVEL: ', self.qtd_de_combustivel)

# Aqui você coloca o código principal
if __name__ == '__main__': 
    my_car = Carro()
    
    my_car.marca = 'Toyota'
    my_car.modelo = 'Corolla'
    my_car.placa = 'RRO4E26'
    my_car.abastecer(10)
    my_car.abastecer(4)
    my_car.abastecer(60)  # Tentando abastecer mais que 30 litros
    my_car.exibir()
