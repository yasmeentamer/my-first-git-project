# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    # THIS IS THE BUG! Should be 'a - b'
    return a + b # Intentional bug: changed to addition!

def multiply(a, b):
    return a * b

# Add this new function
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

print(f"Adding 5 and 3: {add(5, 3)}")
print(f"Subtracting 10 and 4: {subtract(10, 4)}")
print(f"Multiplying 6 and 7: {multiply(6, 7)}")
print(f"Dividing 20 by 5: {divide(20, 5)}")
