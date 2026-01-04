import re

def main():
    print("En az 1 büyük harf, 1 sayı ve 1 özel karakter.")
    password=input("Şifreniz:")
    kontrol=check(password)
    print(kontrol)
    while kontrol=="Güçsüz Şifre Tekrar deneyiniz.":
        password=input("Şifreniz:")
        kontrol=check(password)
        if kontrol=="Güçlü Şifre.Kabul Edildi.":
            print(kontrol)
            return
        print(kontrol)
        
def check(password):
    if re.search(r'[A-Z]+',password) and re.search(r'[0-9]+',password) and re.search(r'[!@#$%^&*(),.?":{}|<>]+',password):
        return f"Güçlü Şifre.Kabul Edildi."
    else:
        return f"Güçsüz Şifre Tekrar deneyiniz."

if __name__=="__main__":
    main()