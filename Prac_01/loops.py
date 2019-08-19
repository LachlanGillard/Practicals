for i in range(1, 21, 2):
    print(i, end=' ')
print()
choice = input("Please choose one option,a,b,c,d: ")
if choice == "a":
    for i in range(0, 101, 10):
        print(i, end=' ')
elif choice == "b":
    for i in range(20, 0, -1):
        print(i, end=' ')
elif choice == "c":
    stars = int(input("Please choose a number: "))
    for i in range(stars):
        print("*")
elif choice == "d":
    stars = int(input("Please choose a number: "))
    for i in range(1, stars + 1):
        print("*" * i)
    print()






