import math

def lcm(numbers):
    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm_result * numbers[i] // math.gcd(lcm_result, numbers[i])
    return lcm_result

def gcd(numbers):
    gcd_result = numbers[0]
    for i in range(1, len(numbers)):
        gcd_result = math.gcd(gcd_result, numbers[i])
    return gcd_result

try:
    N = int(input("N value: "))
    numbers = []
    for i in range(1, N + 1):
        num = int(input("Number {}: ".format(i)))
        numbers.append(num)

    lcm_result = lcm(numbers)
    gcd_result = gcd(numbers)

    print("LCM =", lcm_result)
    print("GCD =", gcd_result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
