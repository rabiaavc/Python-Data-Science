while True: 
    try:    
        boy = float(input("lütfen boyunuzu metre cinsinden giriniz(örn: 1.85): "))
        break
    except ValueError: #sadece value erorr
        print("Lütfen sayıyı doğru giriniz")
while True:
    try:
        kütle = float(input("Lütfen kilonuzu kg cinsinde giriniz(örn:55): "))
        break
    except: # bütün hataları yakalar
        print("Lütfen sayıyı doğru giriniz")

print(kütle/(boy**2))