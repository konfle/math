class rectangle:
    # Oblicza pole prostokąta z wartości podanej przez usera
    a = int(input('Give lenght first side \n'))
    b = int(input('Give lenght second side \n'))
    def set(self, a, b):
        self.a = a
        self.b = b
        return

    def get(self):
        P = self.a * self.b
        print('Filed is: {:.2f}cm^2'.format(P))
        return


# r = rectangle()
# r.get()