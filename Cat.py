class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("meoww")

name = input("Enter the cat's name :")
age = input("Enter the cat's age :")

cat1 = Cat(name,age)
cat1.info()
cat1.make_sound()