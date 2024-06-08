def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

def add(x, n):
    return x + n

def subtract(x, n):
    return x - n

def multiply(x, n):
    return x * n

def divide(x, n):
    if n == 0:
        return "Error: Division by zero"
    return x / n

print("Choose an operation:")
print("1. Power (x^n)")
print("2. Addition (x + n)")
print("3. Subtraction (x - n)")
print("4. Multiplication (x * n)")
print("5. Division (x / n)")
choice = int(input("Enter choice (1/2/3/4/5): "))
   
x = float(input("Enter value for x: "))
n = float(input("Enter value for n: "))
    
if choice == 1:
    print("Result:", power(x, int(n)))
elif choice == 2:
    print("Result:", add(x, n))
elif choice == 3:
    print("Result:", subtract(x, n))
elif choice == 4:
    print("Result:", multiply(x, n))
elif choice == 5:
    print("Result:", divide(x, n))
else:
    print("Invalid choice")
