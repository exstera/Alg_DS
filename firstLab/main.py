from stack import Stack
def shunting_yard_algorithm(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    functions = {'sin', 'cos'}
    output = []
    operator_stack = Stack()

    tokens = expression.split()
    for token in tokens:
        if token in operators:
            while (not operator_stack.is_empty() and operator_stack.peek() in operators and
                   operators[token] <= operators[operator_stack.peek()]):
                output.append(operator_stack.pop())
            operator_stack.push(token)
        elif token in functions:
            operator_stack.push(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            while (not operator_stack.is_empty() and operator_stack.peek() != '('):
                output.append(operator_stack.pop())
            if not operator_stack.is_empty() and operator_stack.peek() == '(':
                operator_stack.pop()
        else:
            output.append(token)

    while not operator_stack.is_empty():
        output.append(operator_stack.pop())

    return output
print(shunting_yard_algorithm(input()))
