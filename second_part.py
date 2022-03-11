class Calculator:

# self is the me of object oriented, each object will have one self

    def __init_(self, num1, num2):  # here we can pass anything to the object
        self.number1 = num1
        self.number2 = num2

    def add(self):
        return self.number1 + self.number2  # we are adding so we are using self to get the inforamtion from

    def update_number2(self, new_num2):
        self.number2 = new_num2


if __name__ == "__main__":
    calc_object = Calculator(15, 30)

# the class will not have self, you use class variable when you are going to share the same value

    print(f"calc_object.number1 = {calc_object.number1}")
    print(f"calc_object.number2 = {calc_object.number2}")
    print(f"calc_object.add = {calc_object.add()}")


    calc_object2 = Calculator(200, 300)  # the init will pass specific values to each objects
    print(f"calc_object.number1 = {calc_object.number1}")
    print(f"calc_object.number2 = {calc_object.number2}")

    calc_object.update_number2(0)
    print(f"calc_object.add = {calc_object.add}")