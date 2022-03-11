class Employee:

    def __init__(self, f_n, l_n, b_y, b_m, b_d, pos, is_grad, id):
        self.first_name = f_n
        self.last_name = l_n
        self.birth_year = b_y
        # self.birth_month = b_m
        # self.birth_day = b_d
        # self.emp_position = pos
        # self.is_graduated = is_grad
        # self.emp_id = id

    def print_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)
    def print_birth_year(self):
        print(self.birth_year)


    #these are the object variables, we can add
    #the object is the name etc

    # def read_first_name(self):
    #     while True:
    #         firstname = input("Please enter your first name: ")
    #         firstname = firstname.strip()
    #         if len(firstname) >= 2:
    #             return firstname
    #     else:
    #         print("First name has to be greater than two characters: ")

#
#
# def main():
#     Employee()
#     read_first_name()
#     set_first_name()



if __name__ == "__main__":


    employee_list = [] # you need a list so you dont lose your variables
    for index in range(4):
        employee_first_name = input("Please enter first name: ")
        employee = Employee(employee_first_name)


        print(employee)
        employee.print_name()


        employee_list.append(employee)
        print("_______________")

        print("The list of employees")
        for employee_variable in employee_list:
            print(employee_variable)
            employee_variable.print_name()
            print("____________")
