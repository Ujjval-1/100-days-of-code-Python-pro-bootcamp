def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum+=n
    return sum

print(add(9,8,7,2,2))


def calculate(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2,add =3, multiply = 5)



class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nissan",model = "GT-R")
print(my_car.model)