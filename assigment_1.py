class Employee:
    name = "Ana"

    def change_name(self):
        self.name = "Rebeca"

employee = Employee()
print(employee.name)
employee.change_name()
print(employee.name)