class Pet:
     def __init__(self, name, age, color):
          self.name = name
          self.age = age
          self.color = color

     def show(self):
          print(f"Hello. I'm {self.name}. I'm {self.age} yars old and have {self.color} color. ")
     def speak(self):
          print("I do not know how to speak yet")

class Cat(Pet):
     def speak(self):
          print("Meow meow")
     
class Dog(Pet):
     def speak(self):
          print("Woof wooof")     