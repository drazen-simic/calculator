import math
import re

# Initialize memory and history
memory = None
history = []


# Function to handle input validation for numbers using regex
def is_valid_number(input_string):
    """Check if the input string is a valid number."""
    pattern = r'^-?\d+(\.\d+)?$'  # Match integers or floating-point numbers
    return re.match(pattern, input_string) is not None


# Function to add operation results to history
def add_to_history(operation, result):
    history.append(f"{operation} = {result}")


# Function to store value in memory
def store_in_memory(value):
    global memory
    memory = value
    print(f"Value {value} stored in memory.")


# Function to recall value from memory
def recall_from_memory():
    if memory is not None:
        print(f"Recalling value from memory: {memory}")
        return memory
    else:
        print("No value stored in memory.")
        return 0  # Return 0 if no value is stored


# Basic calculator functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("Cannot divide by zero.")


def exponentiate(x, y):
    return x ** y


def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        raise ValueError("Cannot calculate square root of negative number.")

# Parse and evaluate basic math expression (simple parsing)
def evaluate_expression(expression):
    """Evaluate a basic mathematical expression with +, -, *, /, and **."""
    try:
        # Check if the expression is valid
        pattern = r'^[\d\+\-\*\/\.\(\)\s]+$'  # Allow numbers, operators, and parentheses
        if re.match(pattern, expression):
            result = eval(expression)  # Safe eval of mathematical expression
            return result
        else:
            print("Invalid expression.")
            return None
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

expression = "(5 + (5 * 5) - 10) ** 2"
# Main calculator loop
def calculator():
    print("Advanced Calculator\n")
    print("Operations: +, -, *, /, sqrt, ** (exponentiation)")
    print("Commands: M+ (store in memory), MR (recall from memory), C (clear history), H (view history), Q (quit)\n")
    
    while True:
        # Get user input
        choice = input("Choose operation or command: ").strip()
        
        match choice.lower():  # Use match-case to handle operations and commands
            case 'q':
                print("Exiting the calculator.")
                break

            case 'h':
                print("\nCalculation History:")
                if history:
                    for entry in history:
                        print(entry)
                else:
                    print("No history available.")
            
            case 'c':
                history.clear()  # Clear history
                print("History cleared.")

            case 'm+':
                try:
                    number = float(input("Enter number to store in memory: "))
                    store_in_memory(number)
                except ValueError:
                    print("Invalid number entered for memory.")

            case 'mr':
                recall_from_memory()

            case 'sqrt':
                try:
                    num = input("Enter number to find square root: ").strip()
                    if is_valid_number(num):
                        num = float(num)
                        result = square_root(num)
                        print(f"Result: {result}")
                        add_to_history(f"sqrt({num})", result)
                    else:
                        print("Invalid number entered.")
                except ValueError as e:
                    print(f"Error: {e}")

            case '+':
                try:
                    num1 = input("Enter first number: ").strip()
                    if not is_valid_number(num1):
                        print("Invalid number.")
                        continue
                    num1 = float(num1)

                    num2 = input("Enter second number: ").strip()
                    if not is_valid_number(num2):
                        print("Invalid number.")
                        continue
                    num2 = float(num2)

                    result = add(num1, num2)
                    print(f"Result: {result}")
                    add_to_history(f"{num1} + {num2}", result)

                except Exception as e:
                    print(f"Error: {e}")

            case '-':
                try:
                    num1 = input("Enter first number: ").strip()
                    if not is_valid_number(num1):
                        print("Invalid number.")
                        continue
                    num1 = float(num1)

                    num2 = input("Enter second number: ").strip()
                    if not is_valid_number(num2):
                        print("Invalid number.")
                        continue
                    num2 = float(num2)

                    result = subtract(num1, num2)
                    print(f"Result: {result}")
                    add_to_history(f"{num1} - {num2}", result)

                except Exception as e:
                    print(f"Error: {e}")

            case '*':
                try:
                    num1 = input("Enter first number: ").strip()
                    if not is_valid_number(num1):
                        print("Invalid number.")
                        continue
                    num1 = float(num1)

                    num2 = input("Enter second number: ").strip()
                    if not is_valid_number(num2):
                        print("Invalid number.")
                        continue
                    num2 = float(num2)

                    result = multiply(num1, num2)
                    print(f"Result: {result}")
                    add_to_history(f"{num1} * {num2}", result)

                except Exception as e:
                    print(f"Error: {e}")

            case '/':
                try:
                    num1 = input("Enter first number: ").strip()
                    if not is_valid_number(num1):
                        print("Invalid number.")
                        continue
                    num1 = float(num1)

                    num2 = input("Enter second number: ").strip()
                    if not is_valid_number(num2):
                        print("Invalid number.")
                        continue
                    num2 = float(num2)

                    result = divide(num1, num2)
                    print(f"Result: {result}")
                    add_to_history(f"{num1} / {num2}", result)

                except Exception as e:
                    print(f"Error: {e}")

            case '**':
                try:
                    num1 = input("Enter base: ").strip()
                    if not is_valid_number(num1):
                        print("Invalid number.")
                        continue
                    num1 = float(num1)

                    num2 = input("Enter exponent: ").strip()
                    if not is_valid_number(num2):
                        print("Invalid number.")
                        continue
                    num2 = float(num2)

                    result = exponentiate(num1, num2)
                    print(f"Result: {result}")
                    add_to_history(f"{num1} ** {num2}", result)

                except Exception as e:
                    print(f"Error: {e}")

            case _ if choice.lower().startswith("calc "):
                expression = choice[5:].strip()  # Extract expression after 'calc '
                result = evaluate_expression(expression)
                if result is not None:
                    print(f"Result: {result}")
                    add_to_history(expression, result)

            case _:
                print("Invalid operation or command. Please try again.")


# Run the calculator
if __name__ == "__main__":
    calculator()
    