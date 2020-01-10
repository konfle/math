class Pyramid:
    # Calculate tetrahedron surface area and capacity
    def __init__(self, side_length):
        self.side_length = side_length

    def get_surface_area(self):
        import math
        square_root_of_3 = math.sqrt(3)
        surface_area = side_length**2 * square_root_of_3
        return surface_area

    def get_capacity_pyramid(self):
        import math
        square_root_of_2 = math.sqrt(2)
        capacity = ((side_length**3) * square_root_of_2) / 12
        return capacity

    def print_information_about_pyramid(self, get_surface_area, get_capacity_pyramid):
        information = f'Tetrahedron has {get_surface_area} cm2 surface area and {get_capacity_pyramid} cm3 volume.'
        return information

class PyramidSecondOption:
    def __init__(self, side_length):
        import math
        self.side_length = side_length
        square_root_of_3 = math.sqrt(3)
        self.surface_area = side_length**2 * square_root_of_3
        square_root_of_2 = math.sqrt(2)
        self.capacity = ((side_length**3) * square_root_of_2) / 12

    def __str__(self):
        return f'Tetrahedron has {self.surface_area:.2f} cm2 surface area and {self.capacity:.2f} cm3 volume.'






'''
    a = int(input('Give a triangle side length \n'))

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
# p = pyramid()
# p.get()
'''