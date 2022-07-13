class Dados:
    def __init__(self, aparelho, modelo, marca):
        self.aparelho = aparelho
        self.modelo = modelo
        self.marca = marca

    def ExibirAp(self):
        print('Aparelho : ',self.aparelho)

    def ExibirModelo(self):
        print('Modelo do aparelho: ',self.modelo)

    def ExibirMarca(self):
        print('A marca do aparelho: ',self.marca)

#objetos
ap1 = Dados('notebook', 'Dell Inspiron i15 M25P', 'Dell')
ap2 = Dados('Celular', 'Iphone', '11pro')
resposta = int(input('Digite 1 ou 2 para exibir Dados de um dos aparelhos: '))

if resposta == 1:
    ap1.ExibirAp()
    ap1.ExibirModelo()
    ap1.ExibirMarca()

elif resposta == 2:
    ap2.ExibirAp()
    ap2.ExibirModelo()
    ap2.ExibirMarca()

