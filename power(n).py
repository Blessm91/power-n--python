# Recursive power function 
def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x, n // 2) ** 2
    else:
        return x * power(x, n - 1)

# Input handling with minimal code
def get_input():
    try:
        x = input("Enter value for x: ")
        x = float(x)
    except ValueError:
        print("Invalid value for x, try again")
        return get_input()
    
    try:
        n = input("n: ")
        n = int(n)
        if n < 0:
            print("Invalid value for n, try again")
            return get_input()
    except ValueError:
        print("Invalid value for n, try again")
        return get_input()
    
    result = power(x, n)
    print(f"{x}^{n} = {result:.4f}")
    
    answer = input("Square another number? (y/n): ")
    if answer.lower().startswith('y'):
        get_input()
    else:
        return

# Main program
print("Need help squaring a number?")  # This displays a message to the user
get_input()