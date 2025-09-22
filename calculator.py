
################################
### Basic console calculator ###
### Includes: + - * /        ###
### Includes: error handling ###
################################


import os


def main():
    while True:
        clear_terminal()
        print("\nCalculator\n")
            
        value_a, value_b = input_values()

        print()

        operation = input("Enter operation: ")

        if is_correct_operation(operation):
            result = calculate(value_a, value_b, operation)

            if result != None:
                print(value_a, operation, value_b, '=', result)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_correct_operation(operation):
    return operation in ['+', '-', '*', '/']

def input_values():
    while True:
        value_a = input("Enter first value: ")

        try:
            value_a = int(value_a)
        except ValueError:
            try:
                value_a = float(value_a)
            except ValueError:
                print("Error: please enter a valid value\n")
                continue

        value_b = input("Enter second value: ")

        try:
            value_b = int(value_b)
            break
        except ValueError:
            try:
                value_b = float(value_b)
                break
            except ValueError:
                print("Error: please enter a valid value\n")
                continue

    return (value_a, value_b)

def calculate(value_a, value_b, operation):
    if operation == '+': 
        return value_a + value_b
    elif operation == '-': 
        return value_a - value_b
    elif operation == '*': 
        return value_a * value_b
    elif operation == '/': 
        if value_b == 0: 
            print("ZeroDivisionError: division by zero\n")
            return None

        result = value_a / value_b

        return int(result) if result.is_integer() else float(result)


if __name__ == '__main__':
    
    main()