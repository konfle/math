# First of all. Comments and everything set in english. Worse english is better than beautifull polish. 

# Classes as a convention we named with capital letter on the begining so you should have Cube. In example:
#  Oval, Math, Pyramid and so on when you have more words in name you just start new word with a capital letter:
# WeatherConditions, BlodPressure, TaxPayment....

class Cube:

    # Thing like this we set outside of classes. Classes are container which should be build the most universal as you can. And specially an input from user it's not a part of class.
    
    # a = int(input('Give a cube edge lenght \n')) <----- I have deleted/comment out this line of code

    # Classes is a blueprint or perscription where you describe how to build, make a unit (object) of class. Class is a perscription itself. It's just description how to build your object.\
    # In python you have constructor which build an object based on description gave by you to computer. Constructor has always the same construction and name of it is:\
    # def __init__(self, ...) dots inside brackets is a place where you put your variables described by you.

    def __init__ (self, edge_of_cube):
        self.edge_of_cube = edge_of_cube

    # __init__ doesn't return anything 

    # method like get has to return something. Here after return should be some variable which gives you what you want to get. Naming a methods you should always try do the most clearest as you can
    # here you want to have TWO methods instead one. One gives a surface area and volume of cube so....

    def get_surface_area (self):
        surface_area = 6 * self.edge_of_cube**2
        return surface_area

    # remember that you can make calculation in return statement so you could avoid line 27 and calculation set after return without making another variable. But now your code is more readible
    # KF: yup I will try uses in other class variable, because I want learn to write clean code.
    def volume_of_cube(self):
        volume = self.edge_of_cube**3
        return volume

    # If you want to use that two method which you create and use it to write description you have to build your own method to print information. Like this:

    def print_information_about_cube(self, get_surface_area, volume_of_cube):
        information = f'Cube has {get_surface_area} cm2 and volume {volume_of_cube} cm3.'
        return information

# Now you have a class blueprint/description so based on it you can build/work on it

'''

# OPTION 1
# You have to invoke/build/create an object based on your description
c = Cube(edge_of_cube=int(input('What is the length of edge cube?')))
# You have to calculate surface area and set to variable
surf = c.get_surface_area()
# You have to calculate volume of cube and set to variable
vol = c.volume_of_cube()
# You have to create information about cube and set to variable
inf = c.print_information_about_cube(surf,vol)
# and then print information to the user
print(inf)

# --------------------------------------------------------------------------------------------------------------

# option 2

# Classes has own build-in methods which are realy helpfull for you as developer
# Here we build __init__ method like this and we have:
'''
class CubeSecondOption:

    def __init__ (self, edge_of_cube):
        self.edge_of_cube = edge_of_cube
        self.surface_area = 6 * self.edge_of_cube**2
        self.volume = self.edge_of_cube**3

# To get description you should use method __str__ to get object description. But here you can get variable from __init__ method since this method doesn't do anything here.

    def __str__(self):
        return f'Cube has {self.surface_area} cm2 and volume {self.volume} cm3.'

# Here based on our blueprint we invoke/build/create an object based on our description set in __init__method and we also set a to 50 units
'''
d = CubeSecondOption(edge_of_cube=int(input('What is the length of edge cube?')))

#because we set __str__method we can just make print(d) to get description

print(d)
'''
