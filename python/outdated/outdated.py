months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Loop forever until user prompts a valid input
while True:
    # Prompt the user for input
    date = input("Date: ")
    try:
        # Split the date by (/)
        x = date.split("/")
        day = x[1]
        month = x[0]
        year = x[2]
        # Check validity of date based on count
        if 1 <= int(day) >= 31 and 1 <= int(month) >= 12:
            break

    except:
        try:
            # Split the date by spaces
            y = date.split(" ")
            nday = y[1]
            nmonth = y[0]
            nyear = y[2]
            # Remove comma from date
            day = nday.replace(",", " ")
            # Identify the month
            for i in range(len(months)):
                if nmonth == months[i]:
                    month = i + 1
            # Check validity of date based on count
            if 1 <= int(day) >= 31 and 1 <= int(month) >= 12:
                break

        except:
            print()
            break

# Check if months or days are less than 10 to add 0
print (day, month, year)