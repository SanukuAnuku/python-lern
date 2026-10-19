from Animal import Animal

class Cat(Animal):
    def __init__(self,name, age):
        super().__init__(name, age)

cat1 = Cat("Marusya",10)
cat2 = Cat("John",11)
print(cat1.__str__(), cat2.__str__())
cat1.speak("Meow")