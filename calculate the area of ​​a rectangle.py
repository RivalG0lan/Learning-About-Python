print("Halo kawan, semoga hari mu menyenankan\nBerikut program untuk menghitung luas persegi panjang, ya !!")
kemauan = input("Mau memulai programnya sekarang? (y/t): ")

while True:  
    if kemauan == 'y':  
        panjangpersegi = float(input("Panjang = "))
        lebarpersegi = float(input("Lebar = "))
        luaspersegipanjang = (panjangpersegi*lebarpersegi)
        if luaspersegipanjang.is_integer() :  
            intluaspersegi = int(luaspersegipanjang)  
            print(f"Luas persegi panjang = {intluaspersegi}")
        else:
            print(f"Luas persegi panjang = {luaspersegipanjang}")

    else:
        print("Baiklah, program berhenti.")
        break 
    
    lagi = input("Mau ngulang lagi gak ? (y/t) = ")
    if lagi != 'y':
        print("Baiklah terimakasih telah menggunakan program ini, God Bless U !") 
        break