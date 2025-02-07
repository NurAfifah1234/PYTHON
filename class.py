class Animal:
    name = ""
    color =""

    def __init__(self, animal_name, animal_color):
        self.name = animal_name
        self.color = animal_color
    def makesound(self, sound):
        print(f"{self.name} with color {self.color} making sound {sound}")
    def eat(self, food):
        print("it is eating", food)
#membuat object dr class
cat = Animal("Taesan", "Black")
panda = Animal("Manda", "clear")

print("------------------------")

print(type(cat))
print(type(panda))

#cat.name = "Taesan"
#cat.color = "Black"
#print(cat.name)
cat.makesound('miaw')
cat.eat("Fish")

panda.name = "manda"
panda.color = "clear"
print(panda.color)

