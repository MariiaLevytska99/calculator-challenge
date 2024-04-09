from strategy.calculator import BinaryCalculator
from strategy.calculator import OperationType


class MultiplyStrategy(BinaryCalculator):
    def __init__(self):
        super().__init__(OperationType.MULTIPLICATION)

    def execute(self, num1, num2):
        return num1 * num2
