class Animal:
    def sound(self):
        print("Animal make sound");
class Dog(Animal):
    def sound(self):
        print("Dog barks");
class Bird(Animal):
    def sound(self):
        print("birds sings");

d=Animal();
d.sound();
