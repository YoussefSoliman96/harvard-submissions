import sys

def main():
    argument_check()
    menu = []
    with open("sicilian.csv", "r") as file:
        for line in file:
            name, price = line.strip().split(",")
            item = {"name": name, "price": price}
            menu.append(item)





def argument_check():
    # Check if command-line arguments are not 2
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if file does not end with .py
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")










if __name__ == "__main__":
    main()