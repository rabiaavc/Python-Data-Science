money = 2000
atm = True

while atm:
    print("1-Para Çekme\n2-Para Yatırma\n3-Kart Billgileri\n4-Kart İade")
    islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

    if islem == "1":
        cekilen_para = int(input("Lütfen Çekmek istedğiniz tutarı giriniz: "))
        if cekilen_para > money:
            print("Bakiyenizi aştınız.")
            continue
        else:
            money = money - cekilen_para
            print("Hesabınızdaki para : {}".format(money))

    elif islem == "2":
        yatırılan_para = int(input("Lütfen yatırmak istediğiniz tutarı giriniz: "))
        money = money + yatırılan_para
        print("Hesabınızdaki para : {}".format(money))

    elif islem == "3":
        print("**Hesap Bilgieriniz***")
        print("""
            Adınız : Rabia
            Soyadınız : AVCI
            IBAN:123476970959567076
            Sahip olduğunuz para: {}
            """.format(money))
        
    elif islem == "4":
        atm = False
        print("Kartınız iade edilecektir.")
        