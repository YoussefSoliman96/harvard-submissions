from datetime import date
import re


def main():
    date = input("Date of Birth: ")
    get_date(date)

def get_date(date):
    new_date = re.search(r"(^[0-9]+)-([0-9]+)-([0-9]+)$", date)
    year, month, day = new_date.split("-")
    print(year, month, day)


if __name__ == "__main__":
    main()