class Pen:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x,y)


    def hello(self):
        print("Hello")

    def hy(self):
        print("HYyy")

point = Pen(10,20)
print(point.x)



# exercise

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def talk(self):
        print(f'Hi iam {self.name}')

john=Person("Gagan Kumar",22)
# print(john.name)
print(john.talk())
print(john.age)
