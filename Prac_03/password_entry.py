"""
Lachlan Gillard
"""
password = input("Password: ")
while len(password) < 6:
    print("Invalid Length")
    password = input("Password: ")
asteriks = '*' * len(password)
print(asteriks)