from math import *


class Integral:

    def __init__(self, polynomial=" ", toSum=" ", exp=1, N=1000, a=0, b=1, coeff=1):

        self.polynomial = polynomial
        self.exp = exp
        self.toSum = toSum
        self.N = N
        self.a = a
        self.b = b
        self.coeff = coeff

        if toSum == " " and polynomial == " ":
            self.getExpression()

    # Integrates a polynomial by separating terms and calculating integrals of each one before adding them together.
    def integratePolynomial(self):
        terms = self.split(self.polynomial)
        result = 0
        for i in terms:
            # Accounts for sin(x) and cos(x)
            if i.strip() == "sin(x)" or i.strip() == "cos(x)":
                temp = Integral(toSum=i.strip(), a=a, b=b, N=N)
                result += temp.integrate()
                # Accounts for x's with coefficieants and exponents
            elif '^' in i:
                temp = Integral(toSum="x^p", coeff=int(i.split('x', 1)[0].strip()),
                                exp=int(i.rsplit('^', 1)[1].strip()),
                                a=a, b=b, N=N)
                result += temp.integrate()
            elif 'x' in i:
                # Accounts for x's with coefficients and no exponents
                try:
                    temp = Integral(toSum="x^p", coeff=int(i.split('x', 1)[0].strip()), exp=1, a=a, b=b, N=N)
                    result += temp.integrate()
                # Accounts for x's with no coefficients and no exponents
                except:
                    temp = Integral(toSum="x^p", coeff=1, exp=1, a=a, b=b, N=N)
                    result += temp.integrate()
            # Accounts for Constants
            else:
                result += int(i) * self.b

        print("The definite integral evaluates to: ", "%.4f" % result)

    def getExpression(self):

        self.toSum = str(input("Enter a function to sum (Choose From x^p, sin(x), or cos(x)): "))

        if self.toSum == "x^p":
            self.exp = int(input("Enter the Exponent for x: "))
            self.coeff = int(input("Enter a coefficient: "))

        self.N = int(input("Number of Calculations (Higher = More Accurate): "))
        self.a = int(input("Enter Lower Bound: "))
        self.b = int(input("Enter Upper Bound: "))

    # Function that defines mathematical function
    def f(self, x):
        if self.toSum == "sin(x)":
            return sin(x)
        elif self.toSum == "cos(x)":
            return cos(x)
        elif self.toSum == "x^p":

            if self.coeff == 1:
                return x ** self.exp
            else:
                return self.coeff * (x ** self.exp)

        else:
            return x

    def split(self, toSplit):
        terms = toSplit.strip().split('+')
        return terms

    def getCoeff(self, toSplit):
        return int(toSplit.split('x', 1)[0].strip())

    def getExp(self, toSplit):
        return int(toSplit.rsplit('^', 1)[1].strip())

    # This needs to run on every term in polynomial
    # integrate(5x^2) + integrate(3x).. etc. then add them together
    def integrate(self):
        value = 0
        # Formula based on Trapezoidal Method for Integral Calculation
        if self.coeff == 1:
            for i in range(1, self.N + 1):
                value += self.f(self.a + ((i - (1 / 2)) * ((self.b - self.a) / self.N)))
        else:
            for i in range(1, self.N + 1):
                value += self.f(self.a + ((i - (1 / 2)) * ((self.b - self.a) / self.N)))

        value2 = abs(((self.b - self.a) / self.N) * value)

        if self.toSum == "x^p" and self.coeff > 1:
            # print("∫", self.coeff, "x ^", self.exp, "dx", " evaluated from ", int(self.a), " to ", int(self.b), " is: ",
            #      "%.4f" % value2)
            return value2
        elif self.toSum == "x^p" and self.coeff <= 1:
            # print("∫", "x ^", self.exp, "dx", " evaluated from ", int(self.a), " to ", int(self.b), " is: ",
            #       "%.4f" % value2)
            return value2
        else:
            # print("∫", self.toSum, "dx", " evaluated from ", int(self.a), " to ", int(self.b), " is: ", "%.4f" % value2)
            return value2


# Keeps Program Running
toQuit = "y"
while toQuit == "y":
    print("\nSING'S SIMPLE DEFINITE INTEGRAL CALCULATOR")
    print("Please note that no coefficients or exponents are allowed on sin(x) or cos(x) just yet.")
    print("Example Expression: 2x^4 + 5x^3 + 4x^2 + 7x + 8 + sin(x)")
    print("Example Expression: sin(x) + 5")
    try:
        expression = str(input("\nPlease enter your expression: "))

        a = int(input("Please enter your lower bound: "))
        b = int(input("Please enter your upper bound: "))
        N = int(input("Please enter your accuracy level (Iterations): "))

        integral = Integral(polynomial=expression, a=a, b=b, N=N)
        integral.integratePolynomial()

        print("\n")

    except:
        print("There was an error with your input. Please try again.")
        print("\n")

    toQuit = str(input("Would you like to perform another calculation? (Type y to continue, anything else to quit): "))
