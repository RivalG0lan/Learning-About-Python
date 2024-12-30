print("Halo User, semoga hari mu menyenankan")

print("Ini adalah program untuk menentukan suatu bilangan ganjil atau genap, ya !!")
kemauan = input("Mau memulai programnya sekarang? (y/t): ")

while True:  
    if kemauan == 'y':  
        bilangan = int(input("Tolong masukkanlah sebuah angka bilangan bulat: "))
        if bilangan % 2 == 0:
            print(f"{bilangan} adalah bilangan genap.")  
        else:
            print(f"{bilangan} adalah bilangan ganjil.")  
    else:
        print("Baiklah, program berhenti.")
        break 

    lagi = input("Mau ngulang lagi gak ? (y/t) = ")
    if lagi != 'y':
        print("Baiklah terimakasih telah menggunakan program ini, God Bless U !") 
        break
