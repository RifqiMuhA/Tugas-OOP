def whileLoopPangkat(angka, pangkat):
    # Jika pangkat 0, maka sudah pasti hasilnya 1
    if pangkat == 0:
        return 1
    else:
        hasil = 1
        i = 0

        # Hitung pangkat angka
        while i < abs(pangkat):
            hasil = hasil * angka
            i = i + 1

        # Seleksi apakah pangkat positif atau negatif
        return positiveOrNegative(pangkat, hasil)

def doWhilePangkat(angka, pangkat):
    # Jika pangkat 0, maka sudah pasti hasilnya 1
    if (pangkat == 0):
        return 1
    else :
        hasil = 1
        i = 0

        # Hitung pangkat angka
        while True:
            hasil = hasil * angka
            i += 1
            if i >= abs(pangkat):break

        # Seleksi apakah pangkat positif atau negatif
        return positiveOrNegative(pangkat, hasil)

def forLoopPangkat(angka, pangkat):
    # Jika pangkat 0, maka sudah pasti hasilnya 1
    if pangkat == 0:
        return 1
    else:
        hasil = 1

        # Hitung pangkat angka2
        for i in range(0, abs(pangkat)):
            hasil = hasil * angka

        # Seleksi apakah pangkat positif atau negatif
        return positiveOrNegative(pangkat, hasil)
           

def positiveOrNegative (pangkat, hasil):
    if pangkat < 0:
        return 1/hasil
    else:
        return hasil   

print("INPUT DATA")
print("==========")
angka = int(input("Masukkan angka\t : "))
pangkat = int(input("Masukkan pangkat : "))

print("\nOUTPUT HASIL")
print("============")
print("Hasil dengan while loop =", whileLoopPangkat(angka, pangkat))
print("Hasil dengan do while   =", doWhilePangkat(angka, pangkat))
print("Hasil dengan for loop   =", forLoopPangkat(angka, pangkat))
