from strategy.calculator import BinaryCalculator
from strategy.calculator import OperationType

class DivideStrategy(BinaryCalculator):

    def __init__(self):
        super().__init__(OperationType.DIVISION)

    def execute(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2
