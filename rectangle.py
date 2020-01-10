class Rectangle:
    # Calculate Rectangle surface area with lengths from user

    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

    def get_surface_area(self):
        surface_area = self.first_side * self.second_side
        return surface_area

    def print_information_about_rectangle(self, get_surface_area):
        information = f'Rectangle has {get_surface_area} cm2 surface area.'
        return information

class RectangleSecondOption:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side
        self.surface_area = first_side * second_side

    def __str__(self):
        return f'Rectangle has {self.surface_area} cm2 surface area.'