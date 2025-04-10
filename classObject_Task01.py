"""
Create Employee class:
instance variables: employee_name, job_title, salary
static_variable : pay_tax

instance method:
__int()__: declares and initializes all the instance variables
__str()__: create string version of the object
work(): display ${employee_name} is working

class method:
display_employee_tax_rate()
"""
import string


class Employee:
    # Static variable
    pay_tax = 0.2 #  tax rate

    # Instance method to initialize instance variables
    def __init__(self,employee_name,job_title,salary):
        self.employee_name = employee_name
        self.job_title = job_title
        self.salary = salary

    # Instance method to create string version of the object
    def __str__(self):
        return f'{type(self).__name__} {self.__dict__}'

    # Instance method to display working status
    def work(self) -> string:
        return f'{self.employee_name} is working'

    # Class method to display employee tax rate
    @classmethod
    def display_employee_tax_rate(cls):
        return f'{cls.pay_tax*100}% Tax Rate'


# Example usage
employee1 = Employee("John","IT Developer",20000)

print(Employee.display_employee_tax_rate())
print(employee1)
print(employee1.work())


