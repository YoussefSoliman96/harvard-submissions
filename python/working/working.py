import re
import sys


def main():
    groups = print(convert(input("Hours: ")))
    time = new_format(groups[0], groups[1], groups[2])
    print(time)


def convert(s):
    format =  re.search(r"^([0-9]+):*([0-5]*) ([A-P]M) to ([0-9]+):*([0-5]*) ([A-P]M)$", s)
    if format:
        groups = format.groups()
        if int(groups[0]) > 12 or int(groups[4]) > 12:
            raise ValueError
        first_output = new_format(groups[0], groups[1], groups[2])
        second_output = new_format(groups[3], groups[4], groups[5])
        return groups, first_output, second_output

    else:
        raise ValueError

def new_format(hour, min, a_p):
    if int(a_p) == "AM":
        if hour == 12:
            new_hour == 00
        else:
            new_hour == hour
    else:
        if hour == 12:
            new_hour == hour
        else:
            new_hour = hour + 12
    if min == None:
        min = ":00"
        time = "{new_hour:02}" + min
    else:
        time = "{new_hour:02}" + ":" + min
    return time



if __name__ == "__main__":
    main()