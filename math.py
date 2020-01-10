import os
from triangle import Triangle, TriangleSecondOption
from quadrat import Quadrat, QuadratSecondOption
from rectangle import Rectangle, RectangleSecondOption
from cube import Cube, CubeSecondOption
from pyramid import Pyramid, PyramidSecondOption
from oval import Oval, OvalSecondOption

# Again, a = int... doesn't tell much to the another developer so i changed on choice
choice = int(input('So what we calculate?\n 1 - Triangle \n 2 - Square \n 3 - Rectangle \n 4 - Cube \n 5 - Tetrahedron \n 6 - Oval \n 0 - Nothing just EXIT \n'))

while choice !=0 :
    
    if choice == 1:
        t = TriangleSecondOption(first_side=int(input('What is the first side length of triangle?\n')), second_side=int(input("What is the second side length of triangle?\n")), third_side=int(input("What is the third side length of triangle?\n")))
        print(t)
        input('Press ENTER to continue')
        os.system('cls')
    elif choice == 2:
        q = QuadratSecondOption(side_length=int(input('What is the side length of square?\n')))
        print(q)
        input('Press ENTER to continue')
        os.system('cls')
    elif choice == 3:
        r = RectangleSecondOption(first_side=int(input('What is the first side of rectangle? \n')), second_side=int(input("What is the second side of rectangle?\n")))
        print(r)
        input('Press ENTER to continue')
        os.system('cls')

        # That is my solution to choosing

    elif choice == 4:

        c = CubeSecondOption(edge_of_cube=int(input('What is the length of edge cube?\n')))
        print(c)
        # KF: I add this input because without user can not see the result when use program in small window
        input('Press Enter to continue')
        os.system('cls')
        
        # and that's all :) 

    elif choice == 5:
        p = PyramidSecondOption(side_length=int(input('What is the side length of tetrahedron? \n')))
        print(p)
        input('Press ENTER to continue')
        os.system('cls')
    elif choice == 6:
        o = OvalSecondOption(first_shaft=int(input('What is the first shaft length of oval?\n')), second_shaft=int(input('What is the second shaft length of oval?\n')))
        print(o)
        input('Press ENTER to continue')
        os.system('cls')
    elif choice == 0:
        print('BYE!')
        break
    else:
        print('Sorry invalid choice. Press ENTER to EXIT') #Need to add an error if user choice is string
        input()
        break
    
    # To give a choice when program is inside a loop you should ask user again about choice

    choice = int(input('So what we calculate?\n 1 - Triangle \n 2 - Square \n 3 - Rectangle \n 4 - Cube \n 5 - Tetrahedron \n 6 - Oval \n 0 - Nothing just EXIT \n'))
