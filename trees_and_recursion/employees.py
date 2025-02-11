"""
Trees can be used for representing hierarchical structures. For example, the personel structure of an organization could be
represented as a tree, where each employee is a node ,and the children of the node are the subordinates of the employee.
"""


class Employee:
    def __init__(self, name, subordinates=[]):
        self.name = name
        self.subordinates = subordinates

    def __repr__(self):
        return self.name


def list_employees(employee, level=0):
    print(" " * (level * 4), employee)

    for subordinates in employee.subordinates:
        list_employees(subordinates, level + 1)


staff = Employee(
    "Emilia",
    [
        Employee("Antti"),
        Employee("Leena", [Employee("Jussi")]),
        Employee("Matti", [Employee("Sasu")]),
    ],
)

list_employees(staff)
"""
    Emilia
    Antti
    Leena
        Jussi
    Matti
        Sasu
"""
