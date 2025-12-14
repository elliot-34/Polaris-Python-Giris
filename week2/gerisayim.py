import time
a=int(input("Bir sayi giriniz: "))
for i in range(a):
    print(f"{a-i} saniye kaldi")
    time.sleep(1)
print("Ateslendi")