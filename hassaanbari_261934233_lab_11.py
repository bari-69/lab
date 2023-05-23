#q1

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def compute_area(self):
        pass

    def __str__(self):
        return self.name


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def compute_area(self):
        return pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def compute_area(self):
        return 0.5 * self.base * self.height


def main():
    Slist = []

    for i in range(3):
        s = input("Enter shape type (c for circle, t for triangle): ")
        if s == "c":
            Slist.append(Circle(int(input("Enter radius: "))))
        elif s == "t":
            Slist.append(Triangle(int(input("Enter base: ")), int(input("Enter height: "))))
        else:
            print("Invalid shape type.")
            continue

        display(Slist[i])


def display(shape):
    print(f"Shape: {shape}")
    print(f"Area: {shape.compute_area()}")


main()

#q2
class Employee:
    def __init__(self, emp_name, emp_id, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary

    def salary_status(self):
        return "Salary: " + str(self.salary)


class BuildingManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 10000)


class ProcurementManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 12000)


class LogisticsManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 15000)


employees = [
    BuildingManager("ahmad", "BM055"),
    ProcurementManager("Jasmine", "PM069"),
    LogisticsManager("mahad", "LM021")
]

for employee in employees:
    print("Employee Name: " + employee.emp_name)
    print("Employee ID: " + employee.emp_id)
    print(employee.salary_status())
    print()
