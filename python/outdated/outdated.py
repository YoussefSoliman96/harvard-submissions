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
    try:
        # Prompt the user for input
        date = input("Date: ")
        # Split the date by (/)
        x = str.split(date, "/")
        day = x[1]
        month = x[0]
        year = x[2]
        print (day, month, year)
        try:
        

        except:

    except ValueError:
        break