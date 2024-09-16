# class student:
#     grade=9
#     print("I am arshey Sharma, I am in grade", grade)
# object=student()
# Activity 2
# class student:
#     grade=9
#     e="Arshey Sharma"
#     def intro(self):
#         print("I am",self.e)
#         print("I am in",self.grade)
# object=student()
# object.intro()
# activity 3
class parrot:
    speces= "Birds"
    def __int__(self,name,age):
        self.name=name
        self.age=age

blue=parrot("blue",10)
green=parrot("green",10)
print("Blue is a {}" .format(blue.speces))
print("Green is a {}" .format(green.speces))