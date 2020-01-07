class pyramid:
    # Oblicza pole i objętość czworościanu foremnego z wartości podanej przez usera
    a = int(input('Give a triangle side lenght \n'))

    def set(self, a):
        self.a = a
        return

    def get(self):
        import math
        x = math.sqrt(3)
        y = math.sqrt(2)
        P = ((self.a ** 2) * x)
        CP = (((self.a ** 3) * y) / 12)
        print('Filed is: {:.2f}cm^2'.format(P))
        print('Capacity is {:.2f}cm^3'.format(CP))
        return
p = pyramid()
p.get()