import math
"""
    This method takes in 3 values from the user and finds the pH of the acid.

                                                             Example: Ka = 1.7*10^-5, concentration = 0.100 M 
                                                                KaDecimal = 1.7,
                                                                powerOfKa = -5,
                                                                concentration = .100
"""
def main():
    KaDecimal = float(input("What is the decimal value of Ka?\n"))
    powerOfKa = int(input("What is the power of 10 for the Ka?\n"))
    concentration = float(input("What is the concentration?\n"))

    x  = math.sqrt((KaDecimal * math.pow(10.0, powerOfKa)) * concentration)

    print("The x value is: " + str(x))
    print("The pH is: " + str(-math.log10(x)))


if __name__ == "__main__":
    main()