"""
    This Class file should help you if you 
        need to have objects in your dataman
"""

class Equation:

    def __init__(self, firstNum, secondNum, operator, answer):
        self.firstNum = firstNum
        self.secondNum = secondNum
        self.operator = operator
        self.answer = answer

    def __str__(self):
        return f'{self.firstNum} {self.operator} {self.secondNum} = {self.answer}'


def main():
    equation = calculation("1 + 3")

    equations = []
    equations.append(Equation(equation[0], equation[1], equation[3], equation[2]))

    print(equations[0].__str__())


def calculation(equation):
    split_equation, return_L = [],[]

# Addition
    if "+" in equation:
        split_equation = equation.split("+")
        x = int(split_equation[0])
        y = int(split_equation[1])
        z = x + y
        return_L.extend((x,y,z))
        return_L.append("+")
        return return_L
    
# Subtraction
    elif "-" in equation:
        split_equation = equation.split("-")
        x = int(split_equation[0])
        y = int(split_equation[1])
        z = x - y
        return_L.extend((x,y,z))
        return_L.append("-")
        return return_L
        
# Division  
    elif "/" in equation:
        split_equation = equation.split("/")
        x = int(split_equation[0])
        y = int(split_equation[1])
        try:
            z = x / y
            return_L.extend((x,y,z))
            return_L.append("/")
            return return_L
        except ZeroDivisionError:
            print("You cannot divide by zero!")
        return
    
# Multiplication
    elif "*" in equation:
        split_equation = equation.split("*")
        x = int(split_equation[0])
        y = int(split_equation[1])
        z = x * y
        return_L.extend((x,y,z))
        return_L.append("*")
        return return_L
    
    elif equation == "exit" or "quit":
        return return_L
    else:
        print("That is not a valid equation.")


if __name__ == "__main__":
    main()
