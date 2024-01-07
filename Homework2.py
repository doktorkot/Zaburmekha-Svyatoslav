class Kit:
    def __init__(self):
        self.energy = 100
        self.happiness = 100

    def play(self):
        self.energy -= 10
        self.happiness += 10


    def sleep(self):
        self.energy += 20

    def eat(self):
        self.energy += 10
        self.happiness += 5

    def be_lonely(self):
        self.happiness -= 10
    def printInfo(self):
        print(self.energy)
        print(self.happiness)
Barsik = Kit()
Barsik.sleep()
Barsik.printInfo()
Barsik.be_lonely()
Barsik.printInfo()
Barsik.eat()
Barsik.printInfo()
