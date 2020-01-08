import os
#from triangle import triangle 
#from quadrat import quadrat 
#from rectangle import rectangle 
from cube import Cube, CubeSecondOption
#from pyramid import pyramid 
#from oval import oval

# Again, a = int... doesn't tell much to the another developer so i changed on choice
choice = int(input('So what we calculate?\n 1 - Triangle \n 2 - Square \n 3 - Rectangle \n 4 - Cube \n 5 - Tetrahedron Shapely \n 6 - Oval \n 0 - Nothing just EXIT \n'))

while choice !=0 :
    
    if choice == 1:
        import triangle
        triangle.triangle()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif choice == 2:
        import quadrat
        quadrat.quadrat()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif choice == 3:
        import rectangle
        rectangle.rectangle()
        input('Press ENTER to continue')
        os.system('cls')
        continue

        # That is my solution to choosing

    elif choice == 4:

        d = CubeSecondOption(edge_of_cube=int(input('What is the length of edge cube?')))
        print(d)
        
        # and that's all :) 

    elif choice == 5:
        import pyramid
        pyramid.pyramid()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif choice == 6:
        import oval
        oval.oval()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif choice == 0:
        print('BYE!')
        break
    else:
        print('Sorry invalid choice. Press ENTER to EXIT')
        input()
        break
    
    # To give a choice when program is inside a loop you should ask user again about choice

    choice = int(input('So what we calculate?\n 1 - Triangle \n 2 - Square \n 3 - Rectangle \n 4 - Cube \n 5 - Tetrahedron Shapely \n 6 - Oval \n 0 - Nothing just EXIT \n'))
