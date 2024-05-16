def calculate(a, b, op):

    result = 0
    
    if(op == "+"):
        result = a+b
    elif(op == "-"):
        result = a-b
    elif(op == "*"):
        result = a*b
    elif(op == "/"):
        result = a/b

    return result