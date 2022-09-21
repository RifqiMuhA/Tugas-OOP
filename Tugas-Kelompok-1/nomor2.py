""" Nama program : nomor2.py
    Nama         : Mohammad Faris Arie Prasetyo, Muhammad Ikhsan Fadhilah, Mohammad Zidan Yohanza, Rifqi Muhadzib Ahdan
    NPM          : 140810190056, 140810210003, 140810210021, 140810210029
    Tanggal buat : 18 September 2022
    Deskripsi    : Spelling angka dengan match_case dan if_else
******************************************************"""

from ast import main, match_case
from difflib import Match

# Fungsi cek range input
def cekRange(nilai):
    if nilai >= 1 and nilai <= 9:
        return False 
    else:
        print("Silakan input nilai sesuai range")
        return True

# Fungsi untuk input angka sesuai range
def input_angka(pesan):
    repeat = True
    while repeat == True :
        angka = int(input(pesan))
        repeat = cekRange(angka)
    return angka

# Fungsi spelling angka 1-9 dengan match_case
def __spellMatchCase(angka):
    match angka:
        case 1:
            return "Satu"
        case 2:
            return "Dua"
        case 3:
            return "Tiga"
        case 4:
            return "Empat"
        case 5:
            return "Lima"
        case 6:
            return "Enam"
        case 7:
            return "Tujuh"
        case 8:
            return "Delapan"
        case 9:
            return "Sembilan"

# Fungsi spelling angka dengan if_else
def __spellIfElse(angka):
    if (angka == 1): return "Satu"
    elif (angka == 2): return "Dua"
    elif (angka == 3): return "Tiga"
    elif (angka == 4): return "Empat"
    elif (angka == 5): return "Lima"
    elif (angka == 6): return "Enam"
    elif (angka == 7): return "Tujuh"
    elif (angka == 8): return "Delapan"
    elif (angka == 9): return "Sembilan"

# main
print("PROGRAM SPELLING 1-9")
print("INPUT DATA")
print("==========")

angka = input_angka("Input angka antara 1-9 : ")

print("\nOUTPUT DATA")
print("===========")
print("Spell (Dengan if else) :", __spellIfElse(angka)) 
print("Spell (Dengan switch)  :", __spellMatchCase(angka))