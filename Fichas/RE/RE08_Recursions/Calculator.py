expr = ((10, '-', 10))



def calculator(expr):
    # base case
    if type(expr) == int:
        return expr
    
    # recursive call
    lhs = calculator(expr[0])
    op = expr[1]
    rhs = calculator(expr[2])
    
    if op == "+":
        return lhs + rhs
    
    if op == "*":
        return lhs * rhs
    
    if op == "-":
        return lhs - rhs
    
    if op == "/":
        return round(lhs / rhs)
    
    
print(calculator(expr))    