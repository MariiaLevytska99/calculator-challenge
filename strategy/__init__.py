from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass
