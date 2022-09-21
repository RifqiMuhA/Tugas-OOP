""" Nama program : nomor4.py
    Nama         : Mohammad Faris Arie Prasetyo, Muhammad Ikhsan Fadhilah, Mohammad Zidan Yohanza, Rifqi Muhadzib Ahdan
    NPM          : 140810190056, 140810210003, 140810210021, 140810210029
    Tanggal buat : 18 September 2022
    Deskripsi    : Menghitung pangkat
******************************************************"""
def hasil_indeks_awal(pangkat) :
    # Terdapat 2 kemungkinan :
    # 1. Jika pangkatnya 0, maka indeks awal loopin pangkat akan melibih jumlah pangkat
    #    Sehingga looping justru tidak akan terjadi
    if pangkat == 0:
        return 1, (pangkat+1)
    # 2. Jika pangkat bukan 0, maka indeks awal dimulai dari 1
    #    Sehingga akan terjadi looping
    else:
        return 1, 1

# Hitung angka berpangkat dengan while_loop
def whileLoopPangkat(angka, pangkat):
    # Tentukan hasil awal sebagai inisiasi perkalian dan indeks awal
    hasil, indeks = hasil_indeks_awal(pangkat)
    while indeks <= abs(pangkat):
        hasil = hasil * angka
        indeks = indeks + 1

    # Seleksi apakah pangkat positif atau negatif
    return positiveOrNegative(pangkat, hasil)

# Fungsi hitung angka berpangkat dengan do while(while loop dengan kondisi true di awal)
def doWhilePangkat(angka, pangkat):
    # Tentukan hasil awal sebagai inisiasi perkalian dan indeks awal
    hasil, indeks = hasil_indeks_awal(pangkat)
    while True:
        if indeks > abs(pangkat):break
        hasil = hasil * angka
        indeks += 1
        
    # Seleksi apakah pangkat positif atau negatif
    return positiveOrNegative(pangkat, hasil)

# Fungsi hitung angka berpangkat dengan for_loop
def forLoopPangkat(angka, pangkat):
    # Tentukan hasil awal sebagai inisiasi perkalian dan indeks awal
    hasil, indeks = hasil_indeks_awal(pangkat)
    for i in range(indeks, abs(pangkat)+1):
        hasil = hasil * angka

    # Seleksi apakah pangkat positif atau negatif
    return positiveOrNegative(pangkat, hasil)  

# Fungsi cek pangkat negatif atau positif
def positiveOrNegative (pangkat, hasil):
    if pangkat < 0:
        return 1/hasil
    else:
        return hasil   

# main 
print("INPUT DATA")
print("==========")
angka = int(input("Masukkan angka\t : "))
pangkat = int(input("Masukkan pangkat : "))

print("\nOUTPUT HASIL")
print("============")
print("Hasil dengan while loop =", whileLoopPangkat(angka, pangkat))
print("Hasil dengan do while   =", doWhilePangkat(angka, pangkat))
print("Hasil dengan for loop   =", forLoopPangkat(angka, pangkat))

