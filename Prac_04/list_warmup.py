numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] = gets number 3
numbers[-1] = gets number 2
numbers[3] = gets number 1 in 4th position
numbers[:-1] = gets all the numbers in the list
numbers[3:4] = gets numbers 1 and 5
5 in numbers = true
7 in numbers = false
"3" in numbers = false
numbers + [6, 5, 3] = numbers.append(6, 5. 3)
"""

numbers[0] = 10
print(numbers[0])
numbers[-1] = 1
print(numbers[-1])
print(numbers[2:])
if 9 in numbers:
    print("True")
else:
    print("False")

