def main():
    print(f"Input is {get_int()}")

def get_int():
    while True:
        try:
            y=int(input("Enter an integer:"))
            return y
        except ValueError:
            pass

main()