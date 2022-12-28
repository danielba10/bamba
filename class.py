class MathOperations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y


math_operation = MathOperations(x=20, y=21)
print(math_operation.minus())
print(math_operation.plus())
print(math_operation.multiply())
print(round(math_operation.divide(), 3))
