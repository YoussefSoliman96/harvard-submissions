def main():
    greeting = input("Input: ").lower()
    greeting = value(greeting)


def value(greeting):
    words = greeting.split(" ")
    first = words[0].replace(",", "")
    if first == "hello":
        print("Output: $0")
    elif greeting[0] == "h":
        print("Output: $20")
    else:
        print("Output: $100")


if __name__ == "__main__":
    main()