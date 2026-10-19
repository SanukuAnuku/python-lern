from oop.Animal import Animal


class Dog(Animal):
    def __init__(self,name, age, breed):
        super().__init__(name, age, breed)

    def defend(self):
        print("Dog is defending")

dog = Dog("Dog",10,"husky")

print(dog.__str__())