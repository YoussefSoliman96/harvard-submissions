due = 50

while due > 0:
    print(f"Amount Due: {due}")
    x = input("Insert Coin: ")
    due = due - int(x)
    change = int(x) - due
    print(f"Change Owed: {change}")
