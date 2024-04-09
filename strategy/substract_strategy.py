from strategy.calculator import BinaryCalculator
from strategy.calculator import OperationType

class SubtractStrategy(BinaryCalculator):
    def __init__(self):
        super().__init__(OperationType.SUBTRACTION)

    def execute(self, num1, num2):
        return num1 - num2
