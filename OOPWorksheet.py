# Python Object-Oriented Programming
import datetime

# OBJECTS

class Employee:

    def __init__(self, first, last, title, salary, security_clearance):
        self.first = first
        self.last = last
        self.title = title
        self.salary = salary
        self.security_clearance = security_clearance
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # @fullname.setter
    # def fullname(self, name):
    #     first, last = name.split(" ")
    #     self.first = first
    #     self.last = last
    #
    # @fullname.deleter
    # def fullname(self):
    #     self.first = None
    #     self.last = None

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, ammount):
        cls.raise_amt = ammount

    @classmethod
    def from_string(cls, emp_str):
       first, last, title, salary, security_clearance = emp_str.split(",")
       return cls(first, last, title, int(salary), bool(security_clearance))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer (Employee):
    raise_amt = 1.10

    def __init__(self, first, last, title, salary, security_clearance, prog_language):
        super().__init__(first, last, title, salary, security_clearance)
        self.prog_language = prog_language

class Manager (Employee):

    def __init__(self, first, last, title, salary, security_clearance, employees=None):
        super().__init__(first, last, title, salary, security_clearance)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

# The following two "magic methods" always go together
    def __repr__(self):
        return Employee("{}", "{}", "{}".format(self.first, self.last, self.salary))

    def __str__(self):
        return "{} - {}".format(self.fullname, self.email)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


# Method help files -
# print(help(Employee))
# print(help(Developer))
# print(help(Manager))


# VARIABLES

# Is today a workday?
my_date = datetime.date(2020, 4, 6)
# print(Employee.is_workday(my_date))

emp_1 = Employee("Test", "Employee1", "Shipping Clerk", 45000,False)
emp_2 = Developer("Test", "Employee2", "Programmer", 75000,True,"Python")
emp_3 = Manager("Test", "Employee3", "IT Director", 100000,True,[emp_1, emp_2])
emp_4 = Manager("Test", "Employee4", "CEO", 150000,True,[emp_1, emp_2, emp_3])

Employee.set_raise_amt(1.05)

# emp_str_1 = "Test,Employee 1,Shipping Clerk,45000,"
# emp_str_2 = "Test,Employee 2,Programmer,75000,"
# emp_str_3 = "Test,Employee 3,IT Director,100000,"
# emp_str_4 = "Test,Employee 4,CEO,150000,"

# emp_1 = Employee.from_string(emp_str_1)
# emp_2 = Employee.from_string(emp_str_2)
# emp_3 = Employee.from_string(emp_str_3)
# emp_4 = Employee.from_string(emp_str_4)
# dev_2 = Developer.from_string(emp_str_2)


# PRINT OPERATIONS
def print_name_salary(Employee):
    print(emp_1.fullname(), "-", emp_1.salary)
    print(emp_2.fullname(), "-", emp_2.salary)
    print(emp_3.fullname(), "-", emp_3.salary)
    print(emp_4.fullname(), "-", emp_4.salary)

# print(print_name_salary(Employee))

def print_raise(Developer):
    print(emp_2.salary)
    emp_2.apply_raise()
    print(emp_2.salary)

# print(emp_2.fullname())
# print(print_raise(emp_2))
# print(emp_2.security_clearance)

def print_name_email(Employee):
    print(emp_1.fullname(),"-\n  Email: ", emp_1.email)
    print(emp_2.fullname(),"-\n  Email: ", emp_2.email)
    print(emp_3.fullname(),"-\n  Email: ", emp_3.email)
    print(emp_4.fullname(),"-\n  Email: ", emp_4.email)

# print(print_name_email(Employee))

# emp_4.print_emp()

# print(isinstance(emp_3, Manager))
# print(issubclass(Manager, Employee))