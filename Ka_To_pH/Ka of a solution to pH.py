import math

# Changes the text colors in the console to make it easier to read
class bcolors:
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

    def disable(self):
        self.OKGREEN = ''
        self.Fail = ''
        self.ENDC = ''

# Collects the user data and performs the appropriate math 
def main():
    ka = getUserFloat("\nWhat is the decimal value of Ka?: ")
    powerOfKa = getUserFloat("\nWhat is the power of 10 for the Ka?: ")
    molarity = getUserFloat("\nWhat is the molarity?: ")
    
    x = math.sqrt((ka * math.pow(10.0, powerOfKa)) * molarity)
    pH = math.log10(x)
    ionization = (x / molarity) * 100

    printSolution(x, pH, ionization)
    
# Collects the users entered data and checks to see if it is valid 
def getUserFloat(message):
    while True:
        try:
           x = float(input(message))
           break
        except:
            print(bcolors.FAIL + "Please enter a valid number!" + bcolors.ENDC) 
    return x

# Prints the calculations 
def printSolution(x, pH, ionization):
    print("\nThe x value is: " + bcolors.OKGREEN + str("%.8f" %x) + bcolors.ENDC)
    print("The pH is: " + bcolors.OKGREEN + str("%.2f" %pH) + bcolors.ENDC)
    print("The ionization is: " + bcolors.OKGREEN + str("%.2f" %ionization) + "%\n" + bcolors.ENDC)


if __name__ == "__main__":
    main()
