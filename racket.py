#! /usr/bin/python3
dict_of_vars = {
}

def add(var1, var2):
    return var1 + var2

def multiply(var1, var2):
    return var1 * var2

def subtract(var1, var2):
    return var1 - var2

def divide(var1, var2):
    return var1 / var2

def evaluate_expression(string):
    ## gets string minus first paren
    currentString = ''
    mode = 0 #0 is op eval, 1 is var1 eval, 2 is var2 eval
    operator = 0
    pos = 0
    length = len(string)
    while pos < length:
        char = string[pos]
        if mode == 1 or mode == 2:
            if char == "(":
                newExpression = ''
                parens = 1
                pos += 1
                while parens != 0:
                    newExpression += string[pos]
                    if string[pos] == "(":
                        parens += 1
                    if string[pos] == ")":
                        parens -= 1
                    pos += 1
                var = evaluate_expression(newExpression)
                if mode == 1:
                    var1 = var
                    mode += 1
                if mode == 2:
                    var2 = var

            elif char == " " or char == ")":
                try:
                    var = int(currentString)
                except:
                    if currentString in dict_of_vars:
                        var = dict_of_vars[currentString]
                    elif operator == 5:
                        new_var = currentString
                        var = -1
                    else:
                        print("{} :is an undefined variable".format(currentString))
                        return True
                if mode == 1:
                    var1 = var
                    currentString = ''
                    mode += 1
                if mode == 2:
                    var2 = var
                    currentString = ''
            else:
                currentString += char

        if mode == 0:
            if char == " " or char  == ")":
                if currentString == "define":
                    operator = 5
                    mode += 1
                    currentString = ''
                elif currentString == "exit":
                    return False
                elif currentString == "+":
                    operator = 1
                    mode += 1
                    currentString = ''
                elif currentString == "*":
                    operator = 2
                    mode += 1
                    currentString = ''
                elif currentString == "-":
                    operator = 3
                    mode += 1
                    currentString = ''
                elif currentString == "/":
                    operator = 4
                    mode += 1
                    currentString = ''
                else:
                    print("{} :this function is not defined".format(currentString))
                    return True
            else:
                if char != "(":
                    currentString += char
        pos += 1

    if operator == 1:
        ans = add(var1, var2)
    elif operator == 2:
        ans = multiply(var1, var2)
    elif operator == 3:
        ans = subtract(var1, var2)
    elif operator == 4:
        ans = divide(var1,var2)
    elif operator == 5:
        dict_of_vars[new_var] = var2
        ans = var2
    else:
        return
    return ans

if __name__ == "__main__":
    run = True
    while run:
        expression = input(">>")
        output = evaluate_expression(expression)
        if type(output) == bool:
            run = output
        else:
            print(output)