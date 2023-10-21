
import math
import time

PI = 3.14159

class Calculator:
    def __init__(self):
        self.fnum = 0
        self.snum = 0
        self.result = 0
        self.angle = 0

    def getdata(self):
        self.fnum = int(input("Enter the First number: "))
        self.snum = int(input("Enter the second number: "))

    def division(self):
        self.getdata()
        if self.snum == 0:
            print("Number cannot be divided by zero!!!")
        else:
            self.result = self.fnum / self.snum
            print(f"{self.fnum} / {self.snum} = {self.result:.2f}")

    def mul(self):
        self.getdata()
        self.result = self.fnum * self.snum
        print(f"{self.fnum} x {self.snum} = {self.result:.2f}")

    def sub(self):
        self.getdata()
        self.result = self.fnum - self.snum
        print(f"{self.fnum} - {self.snum} = {self.result:.2f}")

    def add(self):
        self.getdata()
        self.result = self.fnum + self.snum
        print(f"{self.fnum} + {self.snum} = {self.result:.2f}")

    def exponent(self):
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        result = pow(base, exponent)
        print(f"{base} raised to the power of {exponent} = {result:.2f}")

    def square_root(self):
        n1 = int(input("Enter the number whose square root you want to find: "))
        n2 = math.sqrt(n1)
        print(f"The square root of {n1} is: {n2:.2f}")

    def Sin(self):
        self.angle = float(input("Enter an angle in degrees: "))
        radians = math.radians(self.angle)
        sine = math.sin(radians)
        print(f"Sine: {sine:.2f}")

    def Cos(self):
        self.angle = float(input("Enter an angle in degrees: "))
        radians = math.radians(self.angle)
        cosine = math.cos(radians)
        print(f"Cosine: {cosine:.2f}")

    def Tan(self):
        self.angle = float(input("Enter an angle in degrees: "))
        radians = math.radians(self.angle)
        tangent = math.tan(radians)
        print(f"Tangent: {tangent:.2f}")

    def InverSin(self):
        value = float(input("Enter a value for inverse sine: "))
        inverseSine = math.degrees(math.asin(value))
        print(f"Inverse Sine: {inverseSine:.2f} degrees")

    def InverCos(self):
        value = float(input("Enter a value for inverse cosine: "))
        inverseCosine = math.degrees(math.acos(value))
        print(f"Inverse Cosine: {inverseCosine:.2f} degrees")

    def InverTan(self):
        value = float(input("Enter a value for inverse tangent: "))
        inverseTangent = math.degrees(math.atan(value))
        print(f"Inverse Tangent: {inverseTangent:.2f} degrees")

    def Log(self):
        value = float(input("Enter a value for logarithm: "))
        logarithm = math.log(value)
        print(f"Logarithm: {logarithm:.2f}")

    def Log10(self):
        value = float(input("Enter a value for logarithm with base 10: "))
        logarithmBase10 = math.log10(value)
        print(f"Logarithm (Base 10): {logarithmBase10:.2f}")

if __name__ == "__main__":
    quest = ""
    calc = Calculator()

    print("******************************* Programming Calculator **************************************")
    time.sleep(5)
    print("LOADING........................STARTING...............................................")
    time.sleep(3)
    print("STARTED")
    print()

    while True:
        print("\t\t#############################")
        print("\t\t# WELCOME TO PYTHON CALCULATOR #")
        print("\t\t#############################")

        print("+-------------------+-----------------+----------------------+")
        print("+ 1. Division       + 7. Sin          + 13. Log              +")
        print("+ 2. Multiplication + 8. Cos          + 14. Log with base 10 +")
        print("+ 3. Subtraction    + 9. Tan          +                      +")
        print("+ 4. Addition       + 10. Inverse Sin +                      +")
        print("+ 5. Exponent       + 11. Inverse Cos +                      +")
        print("+ 6. Square root    + 12. Inverse Tan +                      +")
        print("+ 0. Exit           +                 +                      +")
        print("+-------------------+-----------------+----------------------+")

        ch = int(input("Enter the function you want to perform: "))

        if ch == 1:
            calc.division()
        elif ch == 2:
            calc.mul()
        elif ch == 3:
            calc.sub()
        elif ch == 4:
            calc.add()
        elif ch == 5:
            calc.exponent()
        elif ch == 6:
            calc.square_root()
        elif ch == 7:
            calc.Sin()
        elif ch == 8:
            calc.Cos()
        elif ch == 9:
            calc.Tan()
        elif ch == 10:
            calc.InverSin()
        elif ch == 11:
            calc.InverCos()
        elif ch == 12:
            calc.InverTan()
        elif ch == 13:
            calc.Log()
        elif ch == 14:
            calc.Log10()
        elif ch == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

        print()

        quest = input("Do you want to Clear Screen (yes/no)? ")
        if quest.lower() == "yes":
            # This clears the screen in the console
            print("\033c", end="")
