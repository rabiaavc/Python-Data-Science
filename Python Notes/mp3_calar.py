from random import choice
class Mp3Calar():
    def __init__(self, sarki_listesi=None):
        if sarki_listesi is None:
            sarki_listesi = []
        self.suanCalanSarkı = ""
        self.ses = 100
        self.sarki_listesi = sarki_listesi
        self.durum = True

    def sarkisec(self):
        sayac = 1
        for sarki in self.sarki_listesi:
            print(f"{sayac}) {sarki}")
            sayac +=1
        secilen_sarki = int(input("Dinlemek istediğiniz sarki değerini giriniz: "))
        while secilen_sarki < 1 or secilen_sarki > len(self.sarki_listesi):
            secilen_sarki = int(input(f"Secmek istediğiniz sarkinin Doğru değerini giriniz(1-{len(self.sarki_listesi)}): "))
        self.suanCalanSarkı = self.sarki_listesi[secilen_sarki-1]

    def sesArttir(self):
        if self.ses == 100:
            pass
        else:
            self.ses += 10

    def sesAzalt(self):
        if self.ses == 0:
            pass
        else:
            self.ses -= 10


    def rastgeleSarkiSec(self):
        rssec = choice(self.sarki_listesi)
        self.suanCalanSarkı = rssec

    def sarkiEkle(self):
        sanatci = input("Sanatçı/ Grubu giriniz: ")
        sarki = input("Şarkıyı giriniz: ")
        self.sarki_listesi.append(sanatci + " - " + sarki)

    def sarkiSil(self):
        sayac = 1
        for sarki in self.sarki_listesi:
            print(f"{sayac}) {sarki}")
            sayac +=1
        silinecek_sarki = int(input("Silmek istediğiniz sarki değerini giriniz: "))
        while silinecek_sarki < 1 or silinecek_sarki > len(self.sarki_listesi):
            silinecek_sarki = int(input(f"Silmek istediğiniz sarkinin Doğru değerini giriniz(1-{len(self.sarki_listesi)}): "))
        self.sarki_listesi.pop(silinecek_sarki-1)

    def kapat(self):
        self.durum = False

    def menu_goster(self):
        print(f"""
-----Mp3 Çalara Hoşgeldiniz------
Şarkı Listesi: {self.sarki_listesi}
Şu an Çalan Şarkı: {self.suanCalanSarkı}
Ses: {self.ses}

1-) Şarkı Seç
2-) Ses Arttır
3-) Ses Azalt
4-) Rastgele Şarkı Seç
5-) Şarkı Ekle
6-) Sarki Sil
7-) Kapat
""")

    def secim(self):  # `self` parametresi eklendi
        sec = int(input("Seçiminizi Giriniz: "))
        while sec < 1 or sec > 7:
            sec = int(input("Seçtiğiniz değer yanlış, lütfen belirtilen aralıklarda bir değer giriniz (1-7): "))
        return sec

    def calistir(self):
        self.menu_goster()
        secim = self.secim()

        if secim == 1:
            self.sarkisec()
        elif secim == 2:
            self.sesArttir()
        elif secim == 3:
            self.sesAzalt()
        elif secim == 4:
            self.rastgeleSarkiSec()
        elif secim == 5:
            self.sarkiEkle()
        elif secim == 6:
            self.sarkiSil()
        elif secim ==7:
            self.kapat()


# MP3 çalar çalıştırılıyor
my_mp3 = Mp3Calar()
while my_mp3.durum:
    my_mp3.calistir()

print("Program sonlandı.")
