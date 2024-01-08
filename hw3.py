class Student:
    def __init__(self, name):
        self.name = name
        self.grade = 0
        self.smart = 0

    def study(self):
        print(f"{self.name} вивчає матеріал.")
        self.smart += 10

    def take_exam(self):
        print(f"{self.name} складає екзамен.")
        self.grade += 10
    def printInfo(self):
        print(self.smart)
        print(self.grade)
class Teacher:
    def __init__(self, name):
        self.name = name
        self.payment = 0

    def teach(self):
        print(f"{self.name} викладає.")
        self.payment += 10


    def evaluate(self):
        print(f"{self.name} оцінює учня")
        self.payment += 5
    def printPay(self):
        print(self.payment)

me = Student(name="Svyatoslav")
teacher = Teacher(name="Oksana Oleksandrivna")
me.take_exam()
me.printInfo()
teacher.teach()
teacher.evaluate()
teacher.printPay()





        