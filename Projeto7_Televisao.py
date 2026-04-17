class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def power(self):
        if self.ligada: #ja entende como True não precisa == True
            self.ligada = False
        else:
            self.ligada = True      
    def aumenta_canal (self):
        if self.ligada:
            self.canal += 1
        else:
            print ('A Tv está desligada')
    def diminui_canal (self):
        if self.ligada:
            self.canal -= 1
        else:
            print ('A Tv está desligada')


televisao = Televisao()
print ('TV Ligada: {}'.format (televisao.ligada))
televisao.power()
print ('TV Ligada: {}'.format (televisao.ligada))
televisao.power()
print ('TV Ligada: {}'.format (televisao.ligada))
televisao.power() # se identar a linha a tv desliga e o  canal cai no else e não muda pela Tv estar desligada.
print ('TV Ligada: {}'.format (televisao.ligada))
print ('Está no canal: {}'.format (televisao.canal))
televisao.aumenta_canal()
print ('Está no canal: {}'.format (televisao.canal))
televisao.diminui_canal()
print ('Está no canal: {}'.format (televisao.canal))
televisao.aumenta_canal()
print ('Está no canal: {}'.format (televisao.canal))
televisao.diminui_canal()
print ('Está no canal: {}'.format (televisao.canal))

