def divide_or_square(number):
    if number % 5 == 0:
        sqrt=number ** 0.5
        return round(sqrt, 2)
    else:
        rem=number % 5
        return rem

number=int(input('Enter the number: '))
result=divide_or_square(number)
print(result)