# Create a basic class and declare its object


class Car:
    name = "Car"

    def __init__(self, name=None):
        self.name = name


honda = Car("Honda")
print("%s name is %s"%(Car.name,honda.name))