class PyCalculator:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def addition(self):
        return self.arg1 + self.arg2

    def subtraction(self):
        return self.arg1 - self.arg2

    def division(self):
        return self.arg1 / self.arg2

    def multiplication(self):
        return self.arg1 * self.arg2

    def modulus(self):
        return self.arg1 % self.arg2


operation = input(f'Type in what operation you wish to perform of the following options;'
                  f'\n Addition '
                  f'\n Subtraction'
                  f'\n Multiplication'
                  f'\n Division'
                  f'\n Modulus'
                  f'\n_').lower()
number_1 = int(input(f'Type in your first number _'))
number_2 = int(input(f'Type in your second number _'))
py_calculator = PyCalculator(number_1, number_2)

if operation == 'addition':
    print(py_calculator.addition())
elif operation == 'subtraction':
    print(py_calculator.subtraction())
elif operation == 'division':
    print(py_calculator.division())
elif operation == 'multiplication':
    print(py_calculator.multiplication())
elif operation == 'modulus':
    print(py_calculator.modulus())
