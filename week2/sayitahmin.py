import random

def main():
    y=random.randint(1,100)
    guess(y)

def guess(y):
    while True:
        try:
            x=int(input("Guess a number: "))
        except ValueError:
            print("Enter integer numbers only.")
        else:
            if x>y:
                print("Fazla girdiniz,azaltiniz.")
            elif y>x:
                print("Az girdiniz, arttiriniz.")
            else:
                print(f"Tebrikler buldunuz!!! Dogru Sayi {y}'ydi.")
                break

main()