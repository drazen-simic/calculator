import math
import re

# Initialize memory and history
memory = None
history = []

# Helper Functions
def is_valid_number(input_string):
    """Check if the input string is a valid number."""
    pattern = r'^-?\d+(\.\d+)?$'
    return re.match(pattern, input_string) is not None

def get_number(prompt):
    """Prompt the user for a number and validate input."""
    while True:
        num_str = input(prompt).strip()
        if is_valid_number(num_str):
            return float(num_str)
        print("Invalid input! Please enter a valid number.")

def add_to_history(operation, result):
    history.append(f"{operation} = {result}")

def store_in_memory(value):
    global memory
    memory = value
    print(f"Value {value} stored in memory.")

def recall_from_memory():
    if memory is not None:
        print(f"Recalling value from memory: {memory}")
        return memory
    else:
        print("No value stored in memory.")
        return 0

# Basic calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"
def exponentiate(x, y): return x ** y
def square_root(x): return math.sqrt(x) if x >= 0 else "Error: Negative number"

# Unified Operation Handler
def handle_operation(operation, symbol):
    """Generic handler for binary operations."""
    try:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = operation(num1, num2)
        if isinstance(result, str):  # Handle error messages
            print(result)
        else:
            print(f"Result: {result}")
            add_to_history(f"{num1} {symbol} {num2}", result)
    except Exception as e:
        print(f"Error: {e}")

# Handle Calculator Commands
def handle_command(choice):
    if choice == 'h':
        print("\nCalculation History:")
        print("\n".join(history) if history else "No history available.")
    elif choice == 'c':
        history.clear()
        print("History cleared.")
    elif choice == 'm+':
        number = get_number("Enter number to store in memory: ")
        store_in_memory(number)
    elif choice == 'mr':
        recall_from_memory()

# Calculator Logic
def calculator():
    print("Advanced Calculator\n")
    print("Operations: +, -, *, /, sqrt, ** (exponentiation)")
    print("Commands: M+ (store in memory), MR (recall from memory), C (clear history), H (view history), Q (quit)\n")
    
    while True:
        choice = input("Choose operation or command: ").strip().lower()
        
        if choice == 'q':
            print("Exiting the calculator.")
            break
        elif choice in {'h', 'c', 'm+', 'mr'}:
            handle_command(choice)
        elif choice == 'sqrt':
            try:
                num = get_number("Enter number to find square root: ")
                result = square_root(num)
                if isinstance(result, str):  # Handle error messages
                    print(result)
                else:
                    print(f"Result: {result}")
                    add_to_history(f"sqrt({num})", result)
            except Exception as e:
                print(f"Error: {e}")
        elif choice in {'+', '-', '*', '/', '**'}:
            operation_map = {'+': add, '-': subtract, '*': multiply, '/': divide, '**': exponentiate}
            handle_operation(operation_map[choice], choice)
        else:
            print("Invalid operation or command. Please try again.")

# Run the calculator
if __name__ == "__main__":
    calculator()
