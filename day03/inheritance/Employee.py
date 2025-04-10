from day03.inheritance.Person import Person


class Employee(Person):

    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")