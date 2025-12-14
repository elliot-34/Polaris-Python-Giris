a=int(input("Bir sayi giriniz: "))
if a<0:
    print("0'dan girdiginiz negatife:")
    for i in range(-(a+1)):
        print(f"({-i-1})",end="+")
    print(f"({a})=-{int(a*(a-1)/2)}")
elif a==0:
    print("0 girdiniz")
else:
    print("0dan girdiginiz pozitife:")
    for i in range(a-1):
        print(f"{i+1}",end="+")
    print(f"{a}={int(a*(a+1)/2)}")