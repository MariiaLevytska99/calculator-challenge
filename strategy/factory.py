from strategy.add_strategy import AddStrategy
from strategy.substract_strategy import SubtractStrategy
from strategy.multiply_strategy import MultiplyStrategy
from strategy.divide_strategy import DivideStrategy
from strategy.power_strategy import PowerStrategy

class OperationFactory:
    
    @staticmethod
    def get_operation(operator):
        if operator == 'add':
            calculator = AddStrategy()
        elif operator == 'subtract':
            calculator = SubtractStrategy()
        elif operator == 'multiply':
            calculator = MultiplyStrategy()
        elif operator == 'divide':
            calculator = DivideStrategy()
        elif operator == 'power':
            calculator = PowerStrategy()

        return calculator