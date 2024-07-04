def calculator():
    try:
        a = float(input("Enter The First Number: "))
        b = float(input("Enter The Second Number: "))
        c = input("Please Enter the Correct operation (+, -, /, *): ")
        result = 0
        
        # conditions for returning the results
        if c == '+':
            result = a + b
        elif c == '*':
            result = a * b
        elif c == '-':
            result = a - b
        elif c == '/':
            result = a/b
        else:
            print("Invalid Operation !!")
            return
        
        print("Result is:", result)
    
    except ZeroDivisionError :
        print("Cannot Divide By Zero")
    except ValueError:
        print("Please enter only numbers")

calculator()
