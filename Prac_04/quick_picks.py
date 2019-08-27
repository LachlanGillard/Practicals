import random


MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_NUMBERS_IN_LINE = 6
number_of_quick_picks = int(input("How many quick picks?: "))
for i in range(number_of_quick_picks):
    quick_list = []
    while len(quick_list) < NUMBER_OF_NUMBERS_IN_LINE:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in quick_list:
            quick_list.append(number)
    print(sorted("{:2}".format(quick_list)))
