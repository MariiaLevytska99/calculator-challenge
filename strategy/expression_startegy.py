import operator

from strategy.calculator import Calculator

class ExpressionStrategy(Calculator):
    OPERATORS = {
        '+': (operator.add, 1),
        '-': (operator.sub, 1),
        '*': (operator.mul, 2),
        '/': (operator.truediv, 2),
        '^': (operator.pow, 3),
        '(': (None, 0),
        ')': (None, 0)
    }

    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        tokens = self.expression.replace('(', ' ( ').replace(')', ' ) ').split()

        output = []
        operators = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                output.append(float(token))
            elif token in ExpressionStrategy.OPERATORS:
                if token == '(':
                    operators.append(token)
                elif token == ')':
                    while operators[-1] != '(':
                        output.append(operators.pop())
                    operators.pop()
                else:
                    while operators and ExpressionStrategy.OPERATORS[token][1] <= ExpressionStrategy.OPERATORS[operators[-1]][1]:
                        output.append(operators.pop())
                    operators.append(token)

        while operators:
            output.append(operators.pop())

        stack = []
        for token in output:
            if token in ExpressionStrategy.OPERATORS:
                if len(stack) < 2:
                    return 'Invalid expression'
                num2 = stack.pop()
                num1 = stack.pop()
                result = ExpressionStrategy.OPERATORS[token][0](num1, num2)
                stack.append(result)
            else:
                stack.append(token)

        if len(stack) != 1:
            return 'Invalid expression'
        
        result = stack[0]

        return result
