class Person:
    def __init__(self,name,age,power):
        self.name=name
        self.age=age
        self.power=power
    def eat(self):
        self.power=self.power+10

if "__name__" == "__main__":
    p1 = Person("John", 36, 0)
    p2 = Person("Bob",63, 0)

    print(p1.name, "have power:", p1.power)
    p1.eat()
    p1.eat()
    print(p1.name, "have power:", p1.power)


# You are ...
# I want to ...
# 