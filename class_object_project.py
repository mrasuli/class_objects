class Employee:

    def __init__(self, f_n, l_n, b_y, b_m, b_d, pos, is_grad,
                 id):  # the constructor, the method that will be called at the beggining to initialise
        self.first_name = f_n
        self.last_name = l_n
        self.birth_year = b_y
        self.birth_month = b_m
        self.birth_day = b_d
        self.emp_position = pos
        self.is_graduated = is_grad
        self.emp_id = id

    def __str__(self):
        return f"'first_name': '{self.first_name}', 'last_name': '{self.last_name}', 'birth_year':'{self.birth_year}', 'birth_month':'{self.birth_month}', 'birth_day': '{self.birth_day}', 'emp_position':'{self.emp_position}', 'is_graduated': '{self.is_graduated}', 'emp_id': '{self.emp_id}'"


    def get_first_name(self):  # retrieving a value
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_year(self):
        return self.birth_year

    def get_birth_month(self):
        return self.birth_year

    def get_birth_day(self):
        return self.birth_day

    def get_emp_position(self):
        return self.emp_position

    def get_is_graduated(self):
        return self.is_graduated

    def get_emp_id(self):
        return self.emp_id

    def set_first_name(self,
                       first_name):  # to reassign the value to a new value, this is also called encapsulation, you want protect the data
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_birth_year(self, birth_year):
        self.birth_year = birth_year

    def set_birth_month(self, birth_month):
        self.birth_month = birth_month

    def set_birth_day(self, birth_day):
        self.birth_day = birth_day

    def set_emp_position(self, emp_position):
        self.emp_position = emp_position

    def set_is_graduated(self, is_grad):
        self.is_graduated = is_grad

    def set_ids(self, emp_id):
        self.emp_id = emp_id

def read_option_a():
    while True:
        user_option = input("This is a list of your options: add: Add an Employee, remove: Remove an Employee, list: List the Employees ,update: Update Employee Data, exit: Exit the app")
        user_option = user_option.strip()
        if user_option in ["add", "remove", "update", "list", "exit"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")


def read_first_name():
    while True:
        first_name = input("Please Enter The Employee First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, The Employee First Name should be at least 2 Characters")


def read_last_name():
    while True:
        last_name = input("Please Enter The Employee Last Name:")
        last_name = last_name.strip()

        if len(last_name) >= 2:
            return last_name
        else:
            print("Error, The Employee Last Name should be at least 2 Characters")


def read_position():
    while True:
        position = input("Please Enter The Employee Position:")
        position = position.strip()

        if len(position) >= 1:
            return position
        else:
            print("Error, The Employee Position should be at least 1 Characters")


def read_year():
    while True:
        year_str = input("Please Enter the Employee Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Employee Birth Year should be between 1900 and 2004")
        else:
            print("Error, The Employee Birth Year should be a number")


def read_month():
    while True:
        month_str = input("Please Enter the Employee Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Employee Birth Month should be between 1 and 12")
        else:
            print("Error, The Employee Birth Month should be a number")


def read_day():
    while True:
        day_str = input("Please Enter the Employee Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Employee Birth Day should be between 1 and 31")
        else:
            print("Error, The Employee Birth Day should be a number")


def read_is_graduated():
    while True:
        is_graduated_str = input("Have the Employee graduated from the univesity (y/n):")
        is_graduated_str = is_graduated_str.strip()

        if is_graduated_str in ["y", "n"]:
            if is_graduated_str == "y":
                return True
            else:
                return False
        else:
            print("Error, Please Enter y or n")


def read_employee_id():
    while True:
        id_str = input("Please Enter the Employee ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0:
                return id
            else:
                print("Error, The Employee ID should be positive number")
        else:
            print("Error, The Employee ID should be a number")


def create_employee_ob():

    employee_first_name = read_first_name()
    employee_last_name = read_last_name()
    employee_position = read_position()

    employee_birth_year = read_year()
    employee_birth_month = read_month()
    employee_birth_day = read_day()
    employee_is_graduated = read_is_graduated()
    employee_id = read_employee_id()

    employee = Employee(employee_first_name, employee_last_name, employee_birth_year, employee_birth_month,
                        employee_birth_day, employee_position, employee_is_graduated, employee_id)

    return employee


def print_all_employees_data():
    for employee_id_key in all_employees_dict:
        print(f"The data of the employee with Employee_ID = {employee_id_key}")
        print(all_employees_dict[employee_id_key])


def add_employee():
    # global employees_db
    # global employees_counter
    employee = create_employee_ob()
    employees_db[employee.get_emp_id()] = employee
    print("The employee was added to the list")



def remove_employee():
    global employees_db
    remove_id_str = input("PLease enter the iD you would like to remove from the data base: ")
    if remove_id_str.isdigit() and int(remove_id_str) in employees_db:
        remove_id = int(remove_id_str)
    del employees_db[int(remove_id)]
    print(f"The employee with {remove_id} has now been removed from the database.")


def print_employee_db():
    global employees_db

    for entry in employees_db:
        print(employees_db[entry])


def update_employee_data(
        employee_id):  # listen to the video explantion, we need this as an extra information to run parameters
    field_option = read_option()
    if field_option == "first_name":
        new_first_name = read_first_name()
        all_employees_dict[employee_id]["first_name"] = new_first_name
    elif field_option == "last_name":
        new_last_name = read_last_name()
        all_employees_dict[employee_id]["last_name"] = new_last_name
    elif field_option == "employee_position":
        new_position = read_position()
        all_employees_dict[employee_id]["employee_position"] = new_position
    elif field_option == "birth_year":
        new_birth_year = read_year()
        all_employees_dict[employee_id]["birth_year"] = new_birth_year
    elif field_option == "birth_month":
        new_birth_month = read_month()
        all_employees_dict[employee_id]["birth_month"] = new_birth_month
    elif field_option == "birth_day":
        new_birth_day = read_day()
        all_employees_dict[employee_id]["birth_day"] = new_birth_day
    elif field_option == "is_graduated":
        new_is_graduated = read_is_graduated()
        all_employees_dict[employee_id]["is_graduated"] = new_is_graduated
    print(f"Field{field_option} for entry iD {employee_id} has been changed.")


def read_option():
    while True:
        field_option = input("Please Enter the field you want to update: first_name, last_name, position, birth_year, birth_month, birth_day, is_graduated:")
        field_option = field_option.strip()

        if field_option in ["first_name", "last_name", "position", "birth_year", "birth_month", "birth_day",
                            "is_graduated"]:
            return field_option
        else:
            print("Please enter one of the mentioned fields")

    # these are the object variables
    # the object is the name etc


if __name__ == "__main__":

    all_employees_dict = {}
    while True:
        option = read_option_a()

        if option == "add":
            print("The user wants to add an Employee")
            employee_object = create_employee_ob()

            # employee_id = read_employee_id()
            employee_id = employee_object.get_emp_id()

            all_employees_dict[employee_id] = employee_object
            print(all_employees_dict.get(employee_id))
            # print(all_employees_dict)

        elif option == "remove":
            print("The user wants to remove an Employee")
            employee_id = read_employee_id()
            del all_employees_dict[employee_id]

        elif option == "list":
            print("The user wants a list of the employees")
            print_all_employees_data()

        elif option == "update":
            print("The user wants to update the data of an employee")
            employee_id = read_employee_id()
            update_employee_data(employee_id)

        elif option == "exit":
            print("Thanks, see you later")
            break
        else:
            print("Unknown option")
