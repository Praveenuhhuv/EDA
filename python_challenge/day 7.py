def string_range(num):
    return '.'.join(map(str, range(num)))

num = int(input("Enter the number: "))
print(string_range(num))

