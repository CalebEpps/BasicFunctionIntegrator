import re
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

    def trigFunctions(self, polynomial):
        if 'sin' in polynomial:
            getSin = re.findall("sin\(\dx\)", polynomial)
            # tempSin = int(re.search("\d", getSin[0])[0])
            # print(str(tempSin) + "x")
            # print(getSin[0])
            return 1

        elif 'cos' in polynomial:
            getCos = re.findall("cos\(\dx\)", polynomial)
            # tempCos = int(re.search("\d", getCos[0])[0])
            # print(str(tempCos) + "x")
            # print(getCos[0])
            return 2

        elif 'tan' in polynomial:
            getTan = re.findall("tan\(\dx\)", polynomial)
            # tempTan = int(re.search("\d", getTan[0])[0])
            # print(str(tempTan) + "x")
            # print(getTan[0])
            return 3
        else:
            return 0


    # Integrates a polynomial by separating terms and calculating integrals of each one before adding them together.
    def integratePolynomial(self):
        # Remove Spaces
        terms = self.polynomial.replace(" ", "")

        # Define Necessary Lists
        signs = []
        trigFunctions = []
        coeff = []
        exp = []

        # Regex to get signs
        for i in terms:
            if re.match("[+\-*]", i):
                signs.append(i)

        print(trigFunctions)

        # Replace minus signs with 'plus minus'
        terms = terms.replace('-', "+-")

        # Finally split poly by plus sign
        polySplit = terms.split("+")

        print(polySplit)
        for i in polySplit:
            trigFunctions.append(self.trigFunctions(i))
            print(self.trigFunctions(i))

        # loop to gather all coefficients + exponents
        for i in range(len(polySplit)):
            try:
                if trigFunctions[i] != 0:
                    toAppend = ""
                    for c in polySplit[i].split("x")[0]:
                        if c.isdigit():
                            toAppend += c
                            print("C: ", c)
                            print("Post Append: ", str(toAppend))
                    coeff.append(int(toAppend))
                else:
                    coeff.append(int(polySplit[i].split('x')[0].strip()))
            except:
                # Uses error to determine there's no coefficient
                coeff.append(1)
            try:
                exp.append(int(polySplit[i].split('^')[1].strip()))
            except:
                # Uses error to determine there's no exponent
                if 'x' in polySplit[i]:
                    exp.append(1)
                else:
                    exp.append(0)

        # Create 2D list of coeffs and exps
        polyMatrix = [list(i) for i in zip(coeff, exp)]

        # Calculate Integral
        result = 0

        print(polyMatrix)
        print("Terms Length: ", (len(polyMatrix)))

        for i in range(len(polyMatrix)):
            print("Exponent: ", exp[i])
            print("Coefficient: ", coeff[i])
            # Accounts for sin(x) and cos(x)
            if exp[i] > 0:
                if trigFunctions[i] == 0:
                    temp = Integral(toSum="x^p", a=self.a, b=self.b, N=self.N, exp=exp[i], coeff=coeff[i])
                    result += temp.integrate()
                elif trigFunctions[i] == 1:
                    temp = Integral(toSum="sin(x)", a=self.a, b=self.b, N=self.N, exp=exp[i], coeff=coeff[i])
                    result += temp.integrate()
                elif trigFunctions[i] == 2:
                    temp = Integral(toSum="cos(x)", a=self.a, b=self.b, N=self.N, exp=exp[i], coeff=coeff[i])
                    result += temp.integrate()
            else:
                result += self.b * coeff[i]

            print(result)

        print("The definite integral evaluates to: ", "%.4f" % result)
        return result

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
            return (sin(self.coeff * x)) ** self.exp
        elif self.toSum == "cos(x)":
            return (cos(self.coeff * x)) ** self.exp
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
