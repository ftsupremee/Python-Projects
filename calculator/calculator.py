import math
from time import sleep
from simpleeval import simple_eval

def store_calculation(calculation, path: str = "calculations.txt") -> None:
    with open(path, "a") as f:
        f.write("\n" + calculation)

def calculate_expression() -> None:
    expression = input("Enter a math expression: ").replace("^", "**") # simple_eval doesn't accept ^

    # defining allowed functions and constants
    functions = {"sqrt": math.sqrt, "sin": math.sin, 
                 "cos": math.cos, "abs": abs,}
    constants = {"pi": math.pi, "e": math.e}

    # simple_eval is better than eval() for safety and also is better at evaluating expressions
    result = simple_eval(expression, functions = functions, names = constants)

    if isinstance(result, float) and not result.is_integer():
        try:
            decimal_places = int(input("Enter decimal places: "))
            if decimal_places < 0:
                raise ValueError
            calculation = (f"{expression} = {result:.{decimal_places}f}")
            print(calculation)
        except ValueError:
            print("Invalid decimal count, showing full result")
            calculation = (f"{expression} = {result}")
            print(calculation)

    else:
        result = int(result) if isinstance(result, float) else result
        calculation = (f"{expression} = {result}")
        print(calculation)

    # save to file for history
    store_calculation(calculation)

def load_calculations(path: str = "calculations.txt", all: bool = True) -> list[str]:
    with open(path, "r") as f:
        text: list[str] = f.readlines()
    text = [calculation.replace("\n", "") for calculation in text]
    if all:
        return text
    number_of_calculations = int(input("Enter how many calculations you want to look back: "))
    valid = (number_of_calculations < 100 and number_of_calculations < len(text))
    return text[:number_of_calculations] if valid else text[:100]

def main():
    # center python calculator between dashed lines(aesthetics)
    width = 40
    print("-" * width)
    print("PYTHON CALCULATOR".center(width))
    print("-" * width)

    while True:
        choice = int(input("\n1.Evaluate an expression\n2.See history\n3.Quit\nChoose: "))
        match choice:
            case 1:
                calculate_expression()
            case 2:
                print(load_calculations())
            case 3:
                print("Thank you for using this calculator")
                break
            case _:
                print("Please choose a valid option")
        sleep(1) # give users time to read

if __name__ == "__main__":
    main()