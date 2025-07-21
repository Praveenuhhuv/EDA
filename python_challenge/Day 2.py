def convert_add(lst):
    int_lst=list(map(int,lst))
    return (sum(int_lst))

user_input = input("Enter elements separated by space: ").split()
result=convert_add(user_input)
print(result)