def reverse_number(num):
    reverse = 0
    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return reverse

try:
    num = int(input("Number: "))
    reversed_num = reverse_number(abs(num))
    if num < 0:
        reversed_num *= -1
    print("Reverse Number:", reversed_num)
except ValueError:
    print("Invalid input. Please enter a valid number.")
