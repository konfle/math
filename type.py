'''
x=input("gimme int value:")
print(type(x))
c=int(x)
print(type(c))
if type(c) != int:
    print("nope")
else:
    print("ok")
'''

#value = input("Your value here: ")
#list=[ord(value)]
#print(list)

from checkII import check_input
x=check_input(value=input("value:"))
print(x)

