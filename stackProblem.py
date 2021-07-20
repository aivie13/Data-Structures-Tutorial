def calc(text):
    opStack = list()
    for letter in text.split(' '):
        print(opStack)
        if letter == "+" or letter == "-" or letter == "*" or letter == "/" : 
            if len(opStack) < 2:
                print("Not enough numbers")
                return None
            num2 = opStack.pop()
            num1 = opStack.pop()
            if letter == "+": 
                result = num1 + num2
            elif letter == "-": 
                result = num1 - num2
            elif letter == "*": 
                result = num1 * num2
            else:
                if num2 == 0:
                    print("Cannot divide by zero")
                    return None
                result = num1 / num2
            opStack.append(result)
        elif isinstance(float(letter), float): 
            opStack.append(float(letter))
        elif letter == "":
            pass
        else:
            print(letter, "is not a number or operator")
            return None
    if len(opStack) != 1: 
        print("Not enough operators")
        return None
    return opStack[0]

print(calc("7 2 + 6 4 - / 8 *"))