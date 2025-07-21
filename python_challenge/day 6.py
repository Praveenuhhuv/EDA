def user_name(email):
    return email.split('@')[0]
email=input('enter the email: ')
result=user_name(email)
print(result)
