class animal: pass

class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def intro(self):
        print("hello, I am", self.name)


animal = animal('Koala','Gray')

animal.intro()