import math
class Oval:
    # Calculate oval surface area with lengths from user

    def __init__(self, first_shaft, second_shaft):
        self.first_shaft = first_shaft
        self.second_shaft = second_shaft

    def get_surface_area(self):
        surface_area = math.pi * first_shaft * second_shaft
        return surface_area

    def print_information_about_oval(self, get_surface_area):
        information = f'Oval has {get_surface_area} cm2 surface area.'
        return information

class OvalSecondOption:
    def __init__(self, first_shaft, second_shaft):
        self.first_shaft = first_shaft
        self.second_shaft = second_shaft
        self.surface_area = math.pi * first_shaft * second_shaft

    def __str__(self):
        return f'Oval has {self.surface_area:.2f} cm2 surface_area'
