"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output various interesting things, as in the output below.
Note that you can use the functions min, max, sum and len, and you can use the append method to add a number to a list.
"""
numbers = []
number_counter = 1
for i in range(5):
    get_numbers = int(input("Please enter number {}:  ".format(number_counter)))
    numbers.append(get_numbers)
    number_counter += 1
print("The smallest number is: ", min(numbers))
print("The largest number is: ", max(numbers))
print("The sum of all the numbers is: ", sum(numbers))
print("The average of the list is: ", sum(numbers)/len(numbers))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter in your username: ")
if username.lower() in usernames:
    print("Access granted")
else:
    print('Access denied')
