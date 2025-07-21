from datetime import datetime
str1=input("enter the string with dots: ")
def count_dots(str1):
    return str1.count('.')
print("Number of dots:", count_dots(str1))

def age_in_minutes():
    current_year = datetime.now().year
    while True:
        try:
            birth_year = input("Enter your year of birth (4 digits): ")
            if not birth_year.isdigit() or len(birth_year) != 4:
                print("Invalid input! Please enter a 4-digit year.")
                continue

            birth_year = int(birth_year)
            if birth_year < 1900:
                print("Invalid input! Year must be 1900 or later.")
            elif birth_year > current_year:
                print("Invalid input! Year cannot be in the future.")
            else:
                age_years = current_year - birth_year
                age_minutes = age_years * 365 * 24 * 60
                print(f"You are approximately {age_minutes:,} minutes old.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid year.")


age_in_minutes()