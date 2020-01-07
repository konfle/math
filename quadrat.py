class quadrat:
    # Oblicza Pole kwadratu z wartości podanej przez usera
    a = int(input('Give lenght quadrat side \n'))
    def set(self,a):
        self.a = a
        return
    def get(self):
        P=self.a*self.a
        print('Filed is: {:.2f}cm^2'.format(P))
        return
q=quadrat()
q.get()





