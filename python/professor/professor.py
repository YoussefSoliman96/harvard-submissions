import random
def main():
    get_level()


def get_level():
    while True:
        n = int(input("Level: "))
        try:
            if n == 1 or n == 2 or n == 3:
                break
        except:
            pass
        return n


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
