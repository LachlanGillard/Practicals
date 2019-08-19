name = input("Please enter in your name: ")
file_name = open('name.txt', 'w')
print(name, file=file_name)
file_name.close()

file_name = open('name.txt', 'r')
name = file_name.readline()
print("Your name is", name)
file_name.close()

file_name = open('numbers.txt', 'r')
number_1 = int(file_name.readline())
number_2 = int(file_name.readline())
total = number_1 + number_2
print(total)
file_name.close()

total = 0
file_name = open('numbers.txt', 'r')
for line in file_name:
    number = int(line)
    total += number
print(total)
file_name.close()