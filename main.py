# we use object oriented is that we put the data and function in one place
# we move the focus from functionality to the data, we define what is the data not the methods
# we add the functionality after we have set our data
# when you have objects, you know the variables exists within the object

class Calculator:
    number1 = 10 #class variable
    number2 = 20


if __name__ == "__main__":
    calc_object = Calculator()  # this will create an instance of class like a duplicate and will have both number1 and number2. we have brackets to run paramteres

    print(type(calc_object)) # this will show you the type of object
    print(f"calc_object.number 1 = {calc_object.number1}")
    print(f"calc_object.number 2 = {calc_object.number2}")


    calc_object.number1 = 44
    calc_object.number2 = 88

    print("After editing result")
    print(f"calc_object.number 1 = {calc_object.number1}")
    print(f"calc_object.number  2 = {calc_object.number2}")

    calc2 = Calculator()
    print(type(calc2))
    print(f"calc2.number 1 = {calc2.number1}")
    print(f"calc2.number  2 = {calc2.number2}")


    print("Using the class directly")
    print(f"Calculator.number1 = {Calculator.number1}")
    print(f"Calculator.number2 = {Calculator.number2}")
    # you can change the class like bellow
    Calculator.number1 = 33
    Calculator.number2 = 22
    print("After editing")
    print(f"Calculator.number1 = {Calculator.number1}")
    print(f"Calculator.number2 = {Calculator.number2}")

    #whenever you change the class, you change the future and everything on the objects from there on, when you change on th object, it wont change the class

    calc3 = Calculator() # after this class, it will change everything for before and after
    print(type(calc3))
    print(f"calc3.number1 = {calc3.number1}")
    print(f"calc3.number2 = {calc3.number2}")

    print(f"calc2.number1 = {calc2.number1}") # even here the number will change because the class was changed
    print(f"calc2.number2 = {calc2.number2}")

    print(f"calc_object.number 1 = {calc_object.number1}")
    print(f"calc_object.number 2 = {calc_object.number2}")