def main():
    while True:
        try:
            # Get the user's input and run the validate function on it
            card_number = str(input("Number: "))
            if (validate(card_number)) == "Invalid":
                print("INVALID")
            else:
                if (len(card_number)) == 15 and card_number[1] in ["4", "7"]:
                    print("AMEX")
                elif (len(card_number)) == 13 and card_number[0] == "4":
                    print("VISA")
                elif (len(card_number)) == 16:
                    if card_number[0] == "4":
                        print("VISA")
                    else:
                        if int(card_number[1]) in range(1, 6, 1):
                            print("MASTERCARD")
                        else:
                            print("INVALID")
                else:
                    print("INVALID")
            break
        except ValueError:
            print("Invalid input")


# A function that checks whether the user's input is valid or not


def validate(number):
    multiplied = []
    reversed = number[::-1]
    # Identify every other number starting from index 0 then reversing them
    even_positions = [
        reversed[i] for i in filter(lambda a: a % 2 != 0, range(len(reversed)))
    ]
    # multiply every other number by 2
    for j in range(len(even_positions)):
        multiplied.append(int((even_positions[j])) * 2)

    # Modified multiplied with single digits only
    modified = []

    for i in range(len(multiplied)):
        if len(str(multiplied[i])) > 1:
            split = divmod(multiplied[i], 10)
            modified.append(split[0])
            modified.append(split[1])
        else:
            modified.append(multiplied[i])

    # Adding the numbers in the multiplied list together
    even_summed = sum(modified)

    # Identifying every other number that was not multiplied and adding them together
    odd_positions = [
        reversed[i] for i in filter(lambda a: a % 2 == 0, range(len(reversed)))
    ]
    odd_positions = [int(i) for i in odd_positions]
    odd_summed = sum(odd_positions)

    # Adding the 2 sums together
    sum_all = even_summed + odd_summed

    # Getting the last digit
    sum_all = [int(i) for i in str(sum_all)]
    last_digit = sum_all[-1]

    # Return Valid if last digit is "0", otherwise, return Invalid
    if last_digit == 0:
        return "Valid"
    else:
        return "Invalid"


# A function that adds all items in a list and returns the sum


def sum(number):
    summed = 0
    for k in range(len(number)):
        summed += number[int(k)]
    return summed


if __name__ == "__main__":
    main()
