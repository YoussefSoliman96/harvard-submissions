# Take user input
# Loop forever until user input is in the right format (True)
try:
    fraction = input("Fraction: ")
except ValueError:
    print("")
except ZeroDivisionError:
    print("")
x = fraction.split("/")
