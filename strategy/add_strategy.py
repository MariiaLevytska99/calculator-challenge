from strategy.calculator import BinaryCalculator
from strategy.calculator import OperationType


class AddStrategy(BinaryCalculator):
    def __init__(self):
        super().__init__(OperationType.ADDITION)

    def execute(self, num1, num2):
        return num1 + num2
