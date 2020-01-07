import os
count=1
while count !=0 :
    a=int(input('So what we calculate?\n 1 - Triangle \n 2 - Square \n 3 - Rectangle \n 4 - Cube \n 5 - Tetrahedron Shapely \n 6 - Oval \n 0 - Nothing just EXIT \n'))
    if a == 1:
        import triangle
        triangle.triangle()
        input('Press ENTER to continue')
        os.system('cls')
        count += 1
        continue
    elif a == 2:
        import quadrat
        quadrat.quadrat()
        input('Press ENTER to continue')
        os.system('cls')
        count += 1
        continue
    elif a == 3:
        import rectangle
        rectangle.rectangle()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif a == 4:
        import cube
        cube.cube()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif a == 5:
        import pyramid
        pyramid.pyramid()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif a == 6:
        import oval
        oval.oval()
        input('Press ENTER to continue')
        os.system('cls')
        continue
    elif a == 0:
        print('BYE!')
        break
    else:
        print('Sorry invalid choice. Press ENTER to EXIT')
        input()
        break
