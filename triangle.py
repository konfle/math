class Triangle:
    # Calculate triangle surface area with legths from user
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_surface_area(self):
        import math
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
            import math
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
            half_the_circiumference = (first_side + second_side + third_side) / 2
            p = half_the_circiumference
            under_the_square_root = p * (p - first_side) * (p - second_side) * (p - third_side)
            u = under_the_square_root
            self.surface_area = math.sqrt(u)


        def __str__(self):
            return f'Triangle has {self.surface_area:.2f} cm2 surface area.'


'''
    # Obliczanie Pola trójkąta z wartości podanej przez usera
    a = int(input('Give lenght first side called "a"\n'))
    b = int(input('Give lenght side called "b"\n'))
    c = int(input('Give lenght side called "c"\n'))
    L = [a, b, c]
    sortL = sorted(L, reverse=True)
    sumL = sortL[1] + sortL[2]
    highestL = sortL[0]
    #print(sumL)
    #print(highestL)
    if highestL >= sumL:
        print('Condition for building a triangle is not met.\nPlease try again.')
    else:
        print('All length are compile with the condition of building a triangle.')
    def set(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return
    def triangle_filed(self):
        import math
        p = ((self.a + self.b + self.c) / 2)
        p1 = int(p * (p - self.a) * (p - self.b) * (p - self.c))
        P = math.sqrt(p1)
        print('Filed is: {:.2f}cm^2'.format(P))
        return
# t=triangle()
# t.triangle_filed()
'''
