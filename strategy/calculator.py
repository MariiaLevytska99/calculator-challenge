from abc import ABC, abstractmethod
from enum import Enum

class OperationType(Enum):
    NUMBER = 1
    ADDITION = 2
    SUBTRACTION = 3
    MULTIPLICATION = 4
    DIVISION = 5
    POWER = 6

class Calculator(ABC):
    @abstractmethod
    def execute(self, operand1, operand2=None):
        pass
    

class BinaryCalculator(Calculator):
    def __init__(self, operator_type):
        self.operator_type = operator_type

    @abstractmethod
    def execute(self, operand1, operand2):
        pass
