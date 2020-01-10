class Quadrat:
    # Calculate quadrat surface area with side length from user
    def __init__(self, side_length):
        self.side_length = side_length

    def get_surface_area(self):
        surface_area = self.side_length**2
        return surface_area

    def print_information_about_quadrat(self,get_surface_area):
        information = f'Quadrat has {get_surface_area} cm2 surface area.'
        return information

class QuadratSecondOption:

    def __init__(self, side_length):
        self.side_length = side_length
        self.surface_area = side_length**2

    def __str__(self):
        return f'Quadrat has {self.surface_area} cm2 surface area.'





