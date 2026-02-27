class Rocket:
    def __init__(self,name,yakit):
        self.name=name
        self.yakit=yakit
    def yakit_doldur(self,miktar):#yakit azaltmayada izin var, ama eksi olamaz
        self.status("Yakit Miktarinda Degisim")
        if (self.yakit+miktar)<0:
            print("Yakit Miktari Negatif Olamaz. Islem Iptal Ediliyor...")
        else:
            self.yakit+=miktar
            print(f"Yakit Degisimi Basarili. Mevcut Yakit:{self.yakit}")
    def firlat(self):
        self.status("Firlatma")
        if self.yakit>=10:
            self.yakit-=10
            print(f"Firlatma Basarili. Kalan Yakit:{self.yakit}")
        else:
            print(f"Yetersiz Yakit. Mevcut Yakit:{self.yakit}")
    def status(self,islem):
        print(f"\n-----ROCKET STATUS-----")
        print(f"Name={self.name}")
        print(f"Fuel={self.yakit}")
        print(f"Current Operation:{islem}")
        print("----OPERATION RESULT----")
        
def main():
    name=input("Roketinizin Adi:")
    yakit=yakit_al()
    rocket=Rocket(name,yakit)
    while True:
        try:
            print("\n----OPERATIONS MENU----")
            islem=int(input("1-Yakit Doldur\n2-Roketi Firlat\n3-Cikis Yap\nYapmak Istediginiz Islem:"))
        except ValueError:
            print("\n----HATA----\nIslemlerden Birini Seciniz.")
        else:
            match islem:
                case 1:
                    miktar=yakit_al()
                    rocket.yakit_doldur(miktar)
                case 2:
                    rocket.firlat()
                case 3:
                    print("Istek Uzerine Oturum Sonlandiriliyor...")
                    break
                case _:
                    print("\n----HATA----\nIslemlerden Birini Seciniz.")

def yakit_al():
    while True:
        try:
            yakit=int(input("Yakit Miktari:"))
        except ValueError:
            print("Tam Sayi Giriniz.")
        else:
            return yakit
                    
if __name__=="__main__":
    main()