"""
Lachlan Gillard
"""


def main():
    password = get_password()
    asteriks = covert_password_asterisks(password)
    print(asteriks)


def covert_password_asterisks(password):
    asterisks = '*' * len(password)
    return asterisks


def get_password():
    password = input("Password: ")
    while len(password) < 6:
        print("Invalid Length")
        password = input("Password: ")
    return password


main()


