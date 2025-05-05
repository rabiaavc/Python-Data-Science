class Oyun():
    def __init__(self):
        self.tahta = [["","",""],["","",""],["","",""]]
        self.durum = True
        self.hamle = 0

    def oyna(self):
        if self.hamle % 2 == 0:
            self.secim1()
        else:
            self.secim2()

        self.durum = self.oyunKontrol()
        self.hamle += 1

    def secim1(self):
        """
        X koyuyor
        """
        self.tahtaGoster()
        print("Birinci oyuncu, ")
        satir = int(input("Satır giriniz (1-3): ")) - 1
        while satir < 0 or satir > 2:
            satir = int(input("Tekrar satır giriniz (1-3): ")) - 1

        sutun = int(input("Sutun giriniz (1-3): ")) - 1
        while sutun < 0 or sutun > 2:
            sutun = int(input("Tekrar sutun giriniz (1-3): ")) - 1

        if self.dolumu(satir, sutun):
            print("Bu konum dolu! Lütfen başka bir konum seçin.")
            self.secim1()
        else:
            self.tahta[satir][sutun] = "X"

    def secim2(self):
        """
        O koyuyor
        """
        self.tahtaGoster()
        print("İkinci oyuncu, ")
        satir = int(input("Satır giriniz (1-3): ")) - 1
        while satir < 0 or satir > 2:
            satir = int(input("Tekrar satır giriniz (1-3): ")) - 1

        sutun = int(input("Sutun giriniz (1-3): ")) - 1
        while sutun < 0 or sutun > 2:
            sutun = int(input("Tekrar sutun giriniz (1-3): ")) - 1

        if self.dolumu(satir, sutun):
            print("Bu konum dolu! Lütfen başka bir konum seçin.")
            self.secim2()
        else:
            self.tahta[satir][sutun] = "O"

    def tahtaGoster(self):
        for i in self.tahta:
            print(" | ".join(i))
        print("\n")

    def oyunKontrol(self):
        # Yatay kontrol
        for row in self.tahta:
            if row == ["X", "X", "X"] or row == ["O", "O", "O"]:
                return False

        # Dikey kontrol
        for i in range(3):
            if [self.tahta[0][i], self.tahta[1][i], self.tahta[2][i]] == ["X", "X", "X"] or \
               [self.tahta[0][i], self.tahta[1][i], self.tahta[2][i]] == ["O", "O", "O"]:
                return False

        # Çapraz kontrol
        if [self.tahta[0][0], self.tahta[1][1], self.tahta[2][2]] == ["X", "X", "X"] or \
           [self.tahta[0][0], self.tahta[1][1], self.tahta[2][2]] == ["O", "O", "O"]:
            return False

        if [self.tahta[2][0], self.tahta[1][1], self.tahta[0][2]] == ["X", "X", "X"] or \
           [self.tahta[2][0], self.tahta[1][1], self.tahta[0][2]] == ["O", "O", "O"]:
            return False

        return True

    def dolumu(self, satir, sutun):
        return self.tahta[satir][sutun] != ""

# Oyunu çalıştırma
oyun = Oyun()
while oyun.durum:
    oyun.oyna()
    if not oyun.durum:
        print("Oyun Bitti!")
