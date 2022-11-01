import os
def routine():
    # Clean Screen & Banner
    os.system('cls')
    print("\n[-------- Calculator --------]\n")
    
    # Constants
    num1 = input("[1] First Number: ")
    
    while str(num1) == "":
        num1 = input("[ERROR] Invalid Number!\n\tPlease give a new Number: ")
    
    num2 = input("[2] Second Number: ")
    
    while str(num2) == "":
        num2 = input("[ERROR] Invalid Number!\n\tPlease give a new Number: ")
    
    operator = str(input("[O] Operator: "))
    
    while str(operator) == "":
        operator = str(input("[ERROR] Invalid Operator!\n Please give a new Operator: "))
    
    # Variables
    result = None
    
    # Tables
    YES = ["yes", "ye","y"]
    NO = ["no","n"]
    
    # Operator Decision & Calculation
    if operator == ":" or operator == "/" or operator.lower() == "divide":
        result = int(num1) / int(num2)
    elif operator == "*" or operator.lower() == "multiplicate":
        result = int(num1) * int(num2)
    elif operator == "+" or operator.lower() == "plus" or operator.lower() == "add":
        result = int(num1) + int(num2)
    elif operator == "-" or operator == "_" or operator.lower() == "minus" or operator.lower() == "subtract":
        result = int(num1) - int(num2)
    #elif operator == ".":
    #    result = f"{num1}.{num2}"
    else:
        print(f"[ERROR] Your Operator '{operator}' is invalid.")
        
    # Output
    if not result == None:
        print(f"\n[*] {num1} {operator} {num2} = {result}")
    
    # Ask If User Wants To Continue
    check = input("\n[?] Do you want to run another calculation? (Y/n) ")
    val = None
    
    # Check if in YES or NO Table & Decision for Bool
    for i in YES:
        if check.lower() == i:
            val = True

    for i in NO:
        if check.lower() == i:
            val = False
    
    # Run Again or Stop
    if val == True:
        main()
    else:
        exit()

def main():
    routine()

if __name__ == "__main__":
    main()