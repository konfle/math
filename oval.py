class oval:
    # Oblicza Pole owalu z wartości podanej przez usera
    a = int(input('Give lenght first half shaft \n'))
    b = int(input('Give lenght second half shaft \n'))
    def set(self,a,b):
        self.a = a
        self.b = b
        return
    def get(self):
        import math
        p = math.pi
        P= p * self.a * self.b
        print('Filed is: {:.2f}cm^2'.format(P))
        return
# o=oval()
# o.get()
