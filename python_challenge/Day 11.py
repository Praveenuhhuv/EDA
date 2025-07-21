from collections import Counter

def equal_strings(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


num1 = input("Enter 1st string: ").strip().lower()
num2 = input("Enter 2nd string: ").strip().lower()


print(equal_strings(num1, num2))
