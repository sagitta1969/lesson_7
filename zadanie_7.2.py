from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.peram = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        
    @property
    def consumption(self):
        return f'Consumption of fabric for sewing a coat - {round(self.param / 6.5) + 0.5}'

class Costume(Clothes):
    def __init__(self, param):
        super().__init__(param)
        
    @property
    def consumption(self):
        return f'Consumption of fabric for sewing a costume - {2 * self.param + 0.3}'

coat = Coat(42)
costume = Costume(170)
print(coat.consumption)
print(costume.consumption)