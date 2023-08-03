class Animal:
    def animal_sounds(self):
        return "Makes sound"
class Dog(Animal):
    def Dog_sound(self):
        return self.animal_sounds() + " Bow"

class DogColor(Dog):
    def color(self):
        return "color is brown"

dogcolor=DogColor()
print(dogcolor,dogcolor.Dog_sound())
print(dogcolor,dogcolor.color())