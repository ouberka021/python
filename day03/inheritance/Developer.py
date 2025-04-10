from day03.inheritance.Employee import Employee
from day03.inheritance.Tester import Tester


class Developer(Employee):

    def work(self):
        print(f"{self.name} is developing the application")


employee1 = Tester("Sara", 30, "Quality Assurance", 100_000)
employee2 = Developer("Said", 40, "Python Developer", 120_000)

print(employee1)
print(employee2)

employee1.work()
employee2.work()