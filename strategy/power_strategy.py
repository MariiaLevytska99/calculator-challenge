from strategy.calculator import BinaryCalculator
from strategy.calculator import OperationType
import math

class PowerStrategy(BinaryCalculator):
    def __init__(self):
        super().__init__(OperationType.POWER)

    def execute(self, num1, num2):
        return math.pow(num1, num2)
