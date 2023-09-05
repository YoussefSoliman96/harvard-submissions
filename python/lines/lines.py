import sys
def main():
    argument_check()
    # Open the file in command-line
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exit")
    # Loop through each line in the file
    count = 0
    for line in lines :
         if line.isspace():
              count += 1
         if line.lstrip.startswith("#"):
              count += 1
    print(count)



def argument_check():
        # Check if command-line arguments are not 2
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        # Check if file does not end with .py
        elif ".py" not in sys.argv[1]:
            sys.exit("Not a python file")



if __name__ == "__main__":
    main()