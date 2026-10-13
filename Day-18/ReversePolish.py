# Evaluate Reverse Polish Notation:
def EvaluateRPN(tokens):
    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                result = int(a / b)
            stack.append(result)
    return stack[-1]
tokens = ["2", "1", "+", "3", "+"]
print(EvaluateRPN(tokens))