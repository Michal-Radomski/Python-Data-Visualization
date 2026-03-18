"""
This is my first line of comment
This is my second line of comment
"""

# Understanding the power of f-strings
name_planet = "Saturn"
moons_planet = 150
print(f"Planet {name_planet} has {moons_planet} Moons")

# String concatenation
str_1 = "Earth is the only planet with Life."
str_2 = "Maybe not! :D"
print(f"{str_1} {str_2}")  # Earth is the only planet with Life. Maybe not! :D

# Use input() to take user inputs
user_name = input("Enter your name: ")
# Displaying the variable and its type given by the user
print(user_name)
print(type(user_name))

# Ask user to input their fav number
user_fav_number = input("Enter your favourite number: ")
# Display the variable and its type given by the user
print(user_fav_number)
print(type(user_fav_number))  # String

# Convert a string data into integer and float
str_to_int = int(user_fav_number)
print(str_to_int)
print(type(str_to_int))

str_to_float = float(user_fav_number)
print(str_to_float)
print(type(str_to_float))


# Range(start, end, skip) -> Start is inclusive and end is exclusive
range(1, 11, 1)

for index in range(1, 11, 2):
    print(index)


count = 0
while count < 5:
    print(count)
    count += 1


# Define a function to greet a person whose name will be given as an input
def greet_person(name):
    print(
        f"Hey {name}, I hope you are enjoying this session and learning a lot of things in Python!"
    )


# Call that function
greet_person("Mich")


# Create a function that will either add, subtract, multiply or divide two input numbers
def basic_calc(n1, n2, operation):
    """
    Creates a basic calculator that takes n1 and n2 in the same order and performs either of:-
    - add
    - subtract
    - multiply
    - divide

    Parameters -
    -----------
    n1 - first number
    n2 - second number
    operations - any of the operations mentioned above for our basic calc

    Return -
    ------
    The output of the operation done on n1 and n2
    """

    if operation.lower() == "add":
        return n1 + n2
    elif operation.lower() == "subtract":
        return n1 - n2
    elif operation.lower() == "multiply":
        return n1 * n2
    elif operation.lower() == "divide":
        return n1 / n2
    else:
        print(
            f"Operation input can either take: add, multiply, subtract or divide. You gave:- {operation}. Try again"
        )


addition = basic_calc(2, 3, "add")
print(addition)

multiply = basic_calc(3, 3, "multiply")
print(multiply)
