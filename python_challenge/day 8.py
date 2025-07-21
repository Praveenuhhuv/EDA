user_input = list(map(int,input("Enter elements separated by comma: ").split(',')))
user_input.sort()
def odd_even(numbers):
    even_no=[num for num in numbers if num%2==0]
    odd_no=[num for num in numbers if num%2 !=0]
    if not even_no or not odd_no:
        return "List must contain both odd and even numbers."
    return max(even_no)-min(odd_no)
print(odd_even(user_input))