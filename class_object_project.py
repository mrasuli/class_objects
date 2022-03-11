class Employee:

    def __init__(self, f_n, l_n):
        self.first_name = f_n
        self.last_name = l_n
        # self.birth_year = b_y
        # self.birth_month = b_m
        # self.birth_day = b_d
        # self.emp_position = pos
        # self.is_graduated = is_grad
        # self.emp_id = id

    # def update_emp_firstname(self):

    # def __str__(self):
    #     return f"'first_name': '{self.first_name}', 'last_name': '{self.last_name}'"

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    # def print_birth_year(self):
    #     print(self.birth_year)
    # def print_birth_month(self):
    #     print(self.birth_year)
    # def print_birth_day(self):
    #     print(self.birth_day)
    # def print_emp_position(self):
    #     print(self.emp_position)
    # def print_is_graduated(self):
    #     print(self.is_graduated)
    # def print_emp_id(self):
    #     print()

    # these are the object variables, we can add
    # the object is the name etc

    # def read_first_name(self):
    #     while True:
    #         first_name = input("Please enter your first name: ")
    #         first_name = first_name.strip()
    #         if len(first_name) >= 2:
    #             return first_name
    #     else:
    #         print("First name has to be greater than two characters: ")


if __name__ == "__main__":

    employee_list = []  # you need a list so you dont lose your variables
    for index in range(20):  # 20 = to the number of employees you want to reado
        employee_first_name = input("Please enter first name: ")
        employee_last_name = input("Please enter last name: ")
        employee = Employee(employee_first_name, employee_last_name)

        print(employee)
        print(employee.get_first_name())
        print("___________")

        employee_list.append(employee)
        print("_______________")

        print("The list of all employees")
        for employee_variable in employee_list:
            print(employee_variable)
            employee_variable.get_first_name()
            print("____________")
            print(employee_variable.get_last_name())

