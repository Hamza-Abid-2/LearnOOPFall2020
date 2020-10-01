

class animal:
    name = ""
    colour = ""

    def introduceAnimal(self):
        print("Animal Name is " + self.name)
        print("Animal colour is " + self.colour)

    sound = ""
    def speakAnimal(self):
        print("its sound like : " + self.sound)
        print("--------------------------------")

class landAnimal(animal):

    def walk(self):
        print("Animal can walk")

class seaAnimal(animal):

    def swim(self):
        print("Animal can swim")



a1 = landAnimal()
a1.name = "dog"
a1.colour = "black/white/brown"
a1.sound = "wao wao"
a1.walk()
a1.introduceAnimal()
a1.speakAnimal()


a2 = landAnimal()
a2.name = "cat"
a2.colour = "black/white"
a2.sound = "meow"
a2.walk()
a2.introduceAnimal()
a2.speakAnimal()


#----------------------------------
a3 = seaAnimal()
a3.name = "dolphin"
a3.colour = "grey"
a3.sound = "whistles"
a3.swim()
a3.introduceAnimal()
a3.speakAnimal()


a4 = seaAnimal()
a4.name = "turtle"
a4.colour = "brown/black/green"
a4.sound = "hissing"
a4.swim()
a4.introduceAnimal()
a4.speakAnimal()