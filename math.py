import os
from triangle import TriangleSecondOption
from quadrat import QuadratSecondOption
from rectangle import RectangleSecondOption
from cube import CubeSecondOption
from pyramid import PyramidSecondOption
from oval import OvalSecondOption
from inputControl import check_input

# Again, a = int... doesn't tell much to the another developer so i changed on choice
choice = check_input(value=input('So what we calculate?\n 1 - Triangle \n 2 - Square \n 3 - Rectangle \n 4 - Cube \n 5 - Tetrahedron \n 6 - Oval \n 9 - Nothing just EXIT \n'))

while choice[0] !=0 :
    
    if choice[0] == 49:
        t = TriangleSecondOption(first_side=int(input('What is the first side length of triangle?\n')), second_side=int(input("What is the second side length of triangle?\n")), third_side=int(input("What is the third side length of triangle?\n")))
        print(t)
        print('Press ENTER to continue')
        input()
        os.system('cls')
    elif choice[0] == 50:
        q = QuadratSecondOption(side_length=int(input('What is the side length of square?\n')))
        print(q)
        print('Press ENTER to continue')
        input()
        os.system('cls')
    elif choice[0] == 51:
        r = RectangleSecondOption(first_side=int(input('What is the first side of rectangle? \n')), second_side=int(input("What is the second side of rectangle?\n")))
        print(r)
        print('Press ENTER to continue')
        input()
        os.system('cls')
    elif choice[0] == 52:
        c = CubeSecondOption(edge_of_cube=int(input('What is the length of edge cube?\n')))
        print(c)
        print('Press ENTER to continue')
        input()
        os.system('cls')
    elif choice[0] == 53:
        p = PyramidSecondOption(side_length=int(input('What is the side length of tetrahedron? \n')))
        print(p)
        print('Press ENTER to continue')
        input()
        os.system('cls')
    elif choice[0] == 54:
        o = OvalSecondOption(first_shaft=int(input('What is the first shaft length of oval?\n')), second_shaft=int(input('What is the second shaft length of oval?\n')))
        print(o)
        print('Press ENTER to continue')
        input()
        os.system('cls')
    elif choice[0] == 57:
        print('BYE, \n see you soon!')
        break
    else:
        print('Sorry invalid choice. Press ENTER to try again.') #Need to add an error if user choice is string
        input()
    
    # To give a choice when program is inside a loop you should ask user again about choice

    choice = check_input(value=input('So what we calculate?\n 1 - Triangle \n 2 - Square \n 3 - Rectangle \n 4 - Cube \n 5 - Tetrahedron \n 6 - Oval \n 9 - Nothing just EXIT \n'))
