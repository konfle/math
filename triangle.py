class triangle(object):
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
