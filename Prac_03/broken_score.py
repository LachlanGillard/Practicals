"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)


def check_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
        return result
    elif score < 50:
        result = "Bad"
        return result
    elif score < 90:
        result = "Passable"
        return result
    else:
        result = "Exellent"
        return result


main()

