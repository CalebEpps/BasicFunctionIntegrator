from math import *


class Integration:
    toSum = ""
    exp = 1
    N = 100
    # a = lower bound, b = upper bound
    a = 0
    b = 1

    def __init__(self):
        self.toSum = str(input("Enter a function to sum (Choose From x^p, sin(x), or cos(x)): "))
        if self.toSum == "x^p":
            self.exp = int(input("Enter the Exponent for x: "))
        self.N = int(input("Number of Calculations (Higher = More Accurate): "))
        self.a = float(input("Enter Lower Bound: "))
        self.b = float(input("Enter Upper Bound: "))

    # Function that defines mathematical function
    def f(self, x):
        if self.toSum == "sin(x)":
            return sin(x)
        elif self.toSum == "cos(x)":
            return cos(x)
        elif self.toSum == "x^p":
            return x ** self.exp
        else:
            return x

    def integrate(self):
        value = 0

        for i in range(1, self.N + 1):
            value += self.f(self.a + ((i - (1 / 2)) * ((self.b - self.a) / self.N)))

        value2 = abs(((self.b - self.a) / self.N) * value)

        if self.toSum == "x^p":
            print("∫", "x ^", self.exp, "dx", " evaluated from ", int(self.a), " to ", int(self.b), " is: ",
                  "%.4f" % value2)
        else:
            print("∫", self.toSum, "dx", " evaluated from ", int(self.a), " to ", int(self.b), " is: ", "%.4f" % value2)


# Keeps Program Running
toQuit = "y"
while toQuit == "y":
    integration = Integration()
    integration.integrate()
    toQuit = str(input("Would you like to perform another calculation? (Type y to continue, anything else to quit): "))

