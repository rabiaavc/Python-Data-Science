class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True
    def program(self):
        secim  = self.menuSecim()

        if secim == 1:
            self.calisanEkle()
        if secim == 2:
            self.calisanCikar()
        if secim == 3:
            self.verilecekMaasGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()

    def menuSecim(self):
        secim = int(input(f"*****{self.ad} Otomasyonuna Hoşgeldiniz ******\n\n1-Calışan Ekle\n2-Çalışan Çıkar\n3-Verilecek Maaş Goster\n4-Maasları Ver\n5-Masraf Gir\n6-Gelir Gir\n\nSeçiminizi Giriniz: "))
        while secim < 1 or secim > 6:
            secim = int(input("Lütfen 1 ile 6 arasıda bir değer giriniz: "))
        return secim
    
    def calisanEkle():
        
        ad = input("Calışanın adını giriniz: ")
        soyad = input("Calışanın soyadını giriniz: ")
        cinsiyet = input("Calışanın cinsiyetini giriniz: ")
        yas = int(input("Calışanın yaşını giriniz: "))
        maas = int(input("Calışanın maasşını giriniz: "))

        with open("calısanlar.txt","r",encoding = "utf-8") as dosya:
            calisan_listesi = dosya.readlines()
        
        if len(calisan_listesi) == 0:
            id = 1
        else:
            with open("calısanlar.txt","r",encoding = "utf-8") as dosya:
                int(dosya.readlines()[-1].split(")")) + 1

        with open("calısanlar.txt","a+",encoding = "utf-8") as dosya:
            dosya.write(f"{id}){ad}-{soyad}-{yas}-{cinsiyet}-{maas}\n")


        
    def calisanCikar(self):
        with open("calısanlar.txt","r",encoding = "utf-8") as dosya:
            calisanlar = dosya.readlines() 

        gCalisanlar = []

        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))
        for calisan in gCalisanlar:
            print(calisan)
        secim = int(input(f"Lütfen cıkarmak istediğiniz çalışanın numarasını giriniz(1{len(gCalisanlar)})"))
        while secim <1 or secim >len(gCalisanlar):
            secim = int(input("Lütfen (1 - {len(gCalisanlar)} )arasında numara giriniz: "))

        calisanlar.pop(secim -1)

        msayi = len(calisanlar)
        sayac = 1
        dCalisanlar = []

        for calisan in calisanlar:
            dCalisanlar.append(str(sayac) + calisan.split(")")[1])
            sayac += 1

        with open("calısanlar.txt","w",encoding = "utf-8") as dosya:
            dosya.writelines(dCalisanlar)

    def verilecekMaasGoster(self, hesap = "a"):
        """
        hesap a ise aylık
        y ise yıllık
        """
    def maaslariVer(self):
        pass
    def masrafGir(self):
        pass
    def gelirGir(self):
        pass





sirket1 = Sirket("Rabia Avcı")

while sirket1.calisma:
    sirket1.program()