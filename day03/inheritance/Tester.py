from day03.inheritance.Employee import Employee


class Tester(Employee):

    def work(self):
        print(f"{self.name} is testing the application")
