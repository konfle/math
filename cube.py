class cube:
    # Obliczanie pola i objętości sześcianu
    a = int(input('Give a cube edge lenght \n'))
    def set(self, a):
        self.a = a
        return

    def get(self):
        P = 6 * (self.a ** 2)
        CP = self.a ** 3
        print('Filed is: {:.2f}cm^2'.format(P))
        print('Capacity is {:.2f}cm^3'.format(CP))
        return
c = cube()
c.get()