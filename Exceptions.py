from timeit import timeit
# 1. Exceptions
'''
numbers = [1, 2]
print(numbers[3])
'''


'''
age = int(input("Enter your age: "))
'''

# 2. Handling Exceptions
'''
try:
    age = int(input("Enter your age: "))
except ValueError as err:
    print(" you did not enter a valid age")
    print(err)
    print(type(err))
else:
    print("No exceptions were thrown")
print("Execution continues")

'''


# 3. Handling different Exceptions
'''
try:
    age = int(input("Enter age:"))
    xfactor = (10 / age)
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age"
else:
    print("No exceptions were thrown")
'''


# 4. Cleaning up ---> finally clause
# it will execute always whether we have an exception or not
'''

try:
    file = open("app.py")
    age = int(input("Enter the age"))
    xfactor = (10 / 0)
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("No exceptions were thrown")
finally:
    file.close()
'''


# 5. The With Statement(Context Managemnt Protocol)
'''
try:
    with open("app.py") as file:
        print("File opened.")
    age = int(input("Enter the age"))
    xfactor = (10 / 0)
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("No exceptions were thrown")

#when working with multiple files ----->
try:
    with open("app.py") as file, open("another.txt") as target

'''


# 6. Raising Exceptions (raise function)

'''
def calculate_xfactor(age):
    if age <= 10:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

'''


# 7. Cost of Raising Functions
# When writing your own function prefer not to raise exceptions

code1 = """
def calculate_xfactor(age):
    if age <= 10:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass  #--->this doe not do anything but we cannot have an empty except so we use pass


"""

code2 = """
def calculate_xfactor(age):
    if age <= 10:
        return None   #-->none is an object that represents the absence of a value
    return 10 / age



 xfactor = calculate_xfactor(-1)
 if xfactor == None:  # instead of handling exception like in code 1 we can compare
     pass
"""

print("first code =", timeit(code1, number=10000))
print("second code =", timeit(code2, number=10000))
