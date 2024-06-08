numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

prime_count = 0
composite_count = 0

for number in numbers:
    if number > 1:
        is_prime = True
        if number == 2:
            is_prime = True
        elif number % 2 == 0:
            is_prime = False
        else:
            for i in range(3, int(number**0.5) + 1, 2):
                if number % i == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_count += 1
        else:
            composite_count += 1

print(f"Prime numbers count:",prime_count)
print(f"Composite numbers count",composite_count)
