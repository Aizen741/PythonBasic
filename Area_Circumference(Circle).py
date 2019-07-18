
# Area and Circumference of a Circle

class Circle():
    a = int(input("Enter the radius:"))
    pi = 3.14
    def __init__(self,radius=a):
        self.radius = radius
        self.area = radius*radius*self.pi
    def get_circumferemce(self):
        return self.radius *self.pi*2

myCircle = Circle()
print("The radius you givem:", myCircle.radius)
print("The Area is :" ,myCircle.area)
print("The Circumference is :" , myCircle.get_circumferemce())