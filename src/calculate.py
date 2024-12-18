import math


class Calculator:
    def __init__(self):
        self.operations = {
            "add": self.add,
            "sub": self.subtract,
            "mul": self.multiply,
            "square": self.square,
            "log": self.log,
        }

    def calculate(self, operand1, operand2, operator):
        if operator in self.operations:
            try:
                result = self.operations[operator](operand1, operand2)
                return self.format_number(result)
            except ValueError as e:
                return str(e)
        else:
            return "Invalid operator"

    @staticmethod
    def format_number(value):
        return value

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Can not divide by zero!")

        return x / y

    def square(self, x, y):
        return x ** 2

    def log(self, x, y):
        if x <= 0:
            raise ValueError("Error: Logarithm undefined for zero or negative numbers!")
        return math.log10(x)



if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.calculate(10, 5, "+"))  # 15
    print(calculator.calculate(10, 0, "/"))  # Error: Can not divide by zero!
    print(calculator.calculate(4, 0, "square"))  # 16
    print(calculator.calculate(100, 0, "log"))  # 2
    print(calculator.calculate(-1, 0, "log"))
