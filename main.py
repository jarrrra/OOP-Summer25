class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name}({self.age}) lives at {self.address}"

    def myfunc(self):
        print("Hello my name is " + self.name + "! I live at " + self.address)

p1 = Person("Yaraslava Bianko", 18, "[insert some address]")
print(p1)
p1.myfunc()