class Agent:
    def __init__(self,name):
        self.name=name
        self.__islem_sayisi=0
        self.username="NULL"
    def selam_ver(self):
        if self.__islem_sayisi==0:
            self.username=input(f"Merhaba kullanici, yeni tanisiyoruz. Ben {self.name}, sana yardimci olmadan once ismin nedir:").strip()
        print(f"Merhaba {self.username}, ben {self.name}. Sana nasil yardimci olabilirim?")
        self.__islem_sayisi+=1
    def durum_raporu(self):
        print(f"Bugune kadar {self.__islem_sayisi} kadar islem yaptim.")

def main():
    name=input("Asistaninizin adi ne olsun:").strip()
    ajan=Agent(name)
    while True:
        try:
            print("\n----AGENT CHAT----")
            islem=int(input("1-Selam Ver\n2-Islem Sayini Goruntule\n3-Cikis Yap\nYapmak Istediginiz Islem:"))
        except ValueError:
            print("\n----HATA----\nIslemlerden Birini Seciniz.")
        else:
            match islem:
                case 1:
                    ajan.selam_ver()
                case 2:
                    ajan.durum_raporu()
                case 3:
                    print("Istek Uzerine Oturum Sonlandiriliyor...")
                    break
                case _:
                    print("\n----HATA----\nIslemlerden Birini Seciniz.")

if __name__=="__main__":
    main()