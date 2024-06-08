def check_eligibility(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        years_left = 18 - age
        print("You are allowed to vote after ",years_left," years")

try:
    age = int(input("Enter your age: "))
    check_eligibility(age)
except ValueError:
    print("Invalid input. Please enter a valid age.")
