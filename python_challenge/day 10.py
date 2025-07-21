#Task-1
def hide_password():
    user_input = input("Enter the password: ")
    l=len(user_input)
    print('password is',l,' character long')
    return '*'*l
print(hide_password())
#Task-2
def convert_numbers(num_list):
    return [f"{num:,}" for num in num_list]

num =input("Enter a string of numbers: ")
numbers=list(map(int,num.split(',')))
print(convert_numbers(numbers))