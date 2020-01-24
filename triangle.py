import math
class Triangle:
    # Calculate triangle surface area with length from user
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_surface_area(self):
        # Calculating surface area
        half_the_circiumference = (first_side + second_side + third_side) / 2
        p = half_the_circiumference
        under_the_square_root = p * (p - first_side) * (p - second_side) * (p - third_side)
        u = under_the_square_root
        surface_area = math.sqrt(u)
        return surface_area

    def print_information_about_triangle(self,get_surface_area):
        information = f'Triangle has {get_surface_area} cm2 surface area.'
        return information

class TriangleSecondOption:
        def __init__(self, first_side, second_side, third_side):
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
            length = [first_side, second_side, third_side]
            sort_length = sorted(length, reverse=True)
            highest_length = sort_length[0]
            sum_rest_length = sort_length[1] + sort_length[2]
            if highest_length >= sum_rest_length:
                print('Condition for building a triangle is NOT met.\nPlease try again.')
            else:
                print('All length are compile with the condition of building a triangle.')
            half_the_circiumference = (first_side + second_side + third_side) / 2
            p = half_the_circiumference
            under_the_square_root = p * (p - first_side) * (p - second_side) * (p - third_side)
            u = under_the_square_root
            self.surface_area = math.sqrt(u)


        def __str__(self):
            return f'Triangle has {self.surface_area:.2f} cm2 surface area.'
