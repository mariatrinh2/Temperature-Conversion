# This program will be ask the user name,
# ask the temperature, and converting temperatures.
###############################

# Function Definitons
def convert_to_celsius(fahrenheit):
    return(fahrenheit-32)*5/9

# Function Definitons


def convert_to_fahrenheit(celsius):
    return(celsius*9/5) + 32


# beginning program
print('Hello World!')

# prompt the user for their name
print('What is your name?')
myName = input()

# print response
print('It is good to meet you,' + myName)

# ask temperature
print('What conversion would you like me to make?')
print('press 1 for celsius or press 2 for fahrenheit')
mySelect = input()

# ask the temperature conversion methods
print('What is the temperature? ')
myTemp = int(input())


# do something
if mySelect == '1':
    print(convert_to_celsius(myTemp))
elif mySelect == '2':
    print(convert_to_fahrenheit(myTemp))
else:
    print('1:celsius or 2:fahrenheit')
