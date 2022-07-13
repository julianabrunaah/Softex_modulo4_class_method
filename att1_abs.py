
class Viajar:

    def __init__(self, local, malas, hospedagem):
        self.local = local
        self.malas = malas
        self.hospedagem = hospedagem

    def ComprarPassagem(self):
        print('Compre sua passagem para viajar !')
        self.local = str(input('Digite o local para onde pretende ir: '))

    def PrepararMalas(self):
        self.malas = bool(input('Suas malas estão prontas? \nDigite True ou False'))
        if (self.malas) == False:
            print('Faça suas malas agora!')
        elif(self.malas) == True:
            print('Estamos quase lá!')

    def Hospedar(self):

        self.hospedagem = bool(input('Você já definiu sua hospedagem? \nDigite True ou False'))
        if (self.hospedagem) == True:
            print('Tudo pronto!')
            print('Boa viagem!')

        elif (self.hospedagem) == False:
            input('Onde pretende se hospedar? ')
            print('Reserva feita com sucesso!')
            print('Boa viagem!')

viajante1 = Viajar('none', 'none', 'none')
viajante1.ComprarPassagem()
viajante1.PrepararMalas()
viajante1.Hospedar()