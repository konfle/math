class Oval:
    # Calculate oval surface area with lengths from user

    def __init__(self, first_shaft, second_shaft):
        self.first_shaft = first_shaft
        self.second_shaft = second_shaft

    def get_surface_area(self):
        import math
        surface_area = math.pi * first_shaft * second_shaft
        return surface_area

    def print_information_about_oval(self, get_surface_area):
        information = f'Oval has {get_surface_area} cm2 surface area.'
        return information

class OvalSecondOption:
    def __init__(self, first_shaft, second_shaft):
        import math
        self.first_shaft = first_shaft
        self.second_shaft = second_shaft
        self.surface_area = math.pi * first_shaft * second_shaft

    def __str__(self):
        return f'Oval has {self.surface_area:.2f} cm2 surface_area'


'''
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
'''
