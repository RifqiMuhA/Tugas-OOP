""" Nama program : nomor4.py
    Nama         : Mohammad Faris Arie Prasetyo, Muhammad Ikhsan Fadhilah, Mohammad Zidan Yohanza, Rifqi Muhadzib Ahdan
    NPM          : 140810190056, 140810210003, 140810210021, 140810210029
    Tanggal buat : 18 September 2022
    Deskripsi    : Cetak pola asterik dengan nested while_loop dan for_loop
******************************************************"""
# Fungsi cek range input
def cekRange(nilai):
    if nilai > 0:
        return False 
    else:
        print("Silakan input nilai positif")
        return True

# Fumgsi input angka sesuai range
def input_angka(pesan):
    repeat = True
    while repeat == True :
        angka = int(input(pesan))
        repeat = cekRange(angka)
    return angka

# Fungsi untuk mencetak space antar pola
def printSpasi(spasiAwal, indeks):
    for i in range(1, spasiAwal+indeks):
        # Print spasi tanpa new line
        print(" ", end='')

def forLoopAscending(baris, indeks):
    for i in range(0, baris-indeks+1):
        print("*", end='')
    
def forLoopDescending(baris, indeks):
    for i in range(0, indeks):
        print("*", end='')

# Fungsi untuk mencetak pola dengan nested for_loop
def forLoopPola(baris):
    # Looping sebanyak baris dari 1
    for i in range (1, baris+1):
        print(str(i) + ".", end='')
        forLoopAscending(baris, i)

        printSpasi(baris*3, i)

        print(str(i) + ".", end='')
        forLoopDescending(baris, i)
        print('')
    
def whileLoopAscending(baris, indeks):
    while baris >= indeks:
        print('*', end='')
        baris -= 1

def whileLoopDescending(baris, indeks):
    while indeks > 0:
        print('*', end='')
        indeks -= 1

# Fungsi untuk mencetak pola dengan nested while_loop
def whileLoopPola(baris):
    i = 1
    while(i <= baris):
        print(str(i) + ".", end='')
        whileLoopAscending(baris, i)

        printSpasi(baris*3, i)

        print(str(i) + ".", end='')
        whileLoopDescending(baris, i)

        print('')
        i += 1

# main program
baris = input_angka("Masukkan Banyak Baris  : ")
print("Susunan angka dan bintang (Dengan for loop)")
forLoopPola(baris)
print("\nSusunan angka dan bintang (Dengan while loop)")
whileLoopPola(baris)