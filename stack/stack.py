class Stack:
    def __init__(self):
        self.data = []
         

    def push(self,data):
        self.data.append(data)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        return -1
  
def infix_to_postfix(expression):
    precedence = {'+':2,'-':2,'*':3,'/':3}
    operatorStack = Stack()
    currChar = ""
    charList = []
    for char in expression:
        print(char,currChar)
        if char.isalnum():
            currChar += char
        else:
            if currChar != "":
                charList.append(currChar)
                currChar = ""
            charList.append(char)
    if currChar != "":
        charList.append(currChar)
            
    print(charList)

    exper = []
    postfix = []
    for char in charList:
        if char.isalnum():
            postfix.append(char)
        elif char =='(':
            exper.append(char)
        elif char == ')':
            while exper and exper[-1]!= '(':
                print(exper)
                postfix.append(exper.pop())
            exper.pop()
        else :
            while exper and precedence[char] <= precedence.get(exper[-1],0):
                postfix.append(exper.pop())
            exper.append(char)

    while exper:
        postfix.append(exper.pop())
    return postfix

# infixExpr ="a+b*(c*d-e)/f"
# infixExpr2 = "2+5*(1*9-5)/5"
# infixExpr3 = "10+20*(10*82)/20"
# postfixExpr = infix_to_postfix(infixExpr3)
# print(postfixExpr)

def Solve_expression(expression):
    stack = []
    operators = set(['+','-','*','/'])
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            stack.append(result)
        
  
exper = "34+2*7"
result = Solve_expression(exper)
print(result)
                

            


# stack = Stack()
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# print(stack.data)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.data)


