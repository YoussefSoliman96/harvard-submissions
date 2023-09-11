import csv
import sys
from datetime import datetime


def main():
    # Get all the clients' data
    clients_data = read_file()
    # Extract all the clients' names out of the file
    # Get the requested client's data
    client_data = get_data(clients_data)
    # Get the requested client's first name, last name, email and balance
    first = (client_data["first_name"])
    last = (client_data["last_name"])
    email = (client_data["email"])
    balance = (client_data["balance"])
    # Display the list of options to the current client
    print(options())


    class Client:
        def __init__(self, first_name, last_name, email, balance):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.balance = balance

        def __str__(self):
            amount = self.balance + "💲"
            return amount

        def deposit(self, cash):
            self._balance += cash

        def withdraw(self, cash):
            self._balance -= cash


    client = Client(first, last, email, balance)






# Read the file containing clients' data
def read_file():
    clients = []
    try:
        # Open the file containing clients' data
        with open("clients.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Loop through the file and append data to the clients stack
            for line in csv_reader:
                clients.append({'first_name': line["first_name"], 'last_name': line["last_name"], 'email': line["email"], 'balance': line["balance"]})
        return clients
    except FileNotFoundError:
        sys.exit("File not found")

# Display options of what the client can do
def options():
    choices = ["Deposit", "Withdraw", "Print statement"]
    choice = print("What do you want to do:")
    for idx, element in enumerate(choices):
        print("{}) {}".format(idx+1,element))
    while True:
        i = input("Enter number: ")
        try:
            if 0 < int(i) <= len(choices):
                return choices[i]
        except ValueError:
            pass


# Get the a certain client's data
def get_data(client_data):
    # Loop forever untill the user inputs a valid name or (Control-d)
    while True:
        try:
            # Take user's input of a certain client's name
            client_search = input("Client name: ")
            # Get the first name and the last name
            full_name = client_search.split(" ")
            if len(full_name) < 2:
                print("Missing lastname")
            # Loop through all the client names untill you find the client then return the data
            for name in client_data:
                try:
                    if (name["first_name"] == full_name[0]) & (name["last_name"] == full_name[1]):
                        return(name)
                except IndexError:
                    pass
        except EOFError:
            sys.exit("User input invalid")



if __name__ == "__main__":
    main()



"""


def get_date():







def withdraw():



def calculate_balance():

"""