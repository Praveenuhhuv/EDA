user_input = input("Enter a string of numbers: ")
def biggest_odd(numbers):
    odd_lst = [int(num) for num in numbers if int(num) % 2 != 0]
    return max(odd_lst) if odd_lst else "No odd numbers found"

print(biggest_odd(user_input))
