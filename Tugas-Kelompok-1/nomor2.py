from ast import match_case
from difflib import Match

def cekRange(nilai):
    if nilai >= 0 and nilai <= 9:
        return False 
    else:
        print("Silakan input nilai sesuai range")
        return True

def __spellMatchCase(angka):
    match angka:
        case 0:
            return "Nol" 
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

def __spellIfElse(angka):
    if (angka == 0): return "Nol"
    elif (angka == 1): return "Satu"
    elif (angka == 2): return "Dua"
    elif (angka == 3): return "Tiga"
    elif (angka == 4): return "Empat"
    elif (angka == 5): return "Lima"
    elif (angka == 6): return "Enam"
    elif (angka == 7): return "Tujuh"
    elif (angka == 8): return "Delapan"
    elif (angka == 9): return "Sembilan"


print("PROGRAM SPELLING 1-9")
print("INPUT DATA")
print("==========")

repeat = True
while repeat == True :
    angka = int(input("Input angka antara 1-9 : "))
    repeat = cekRange(angka)

print("\nOUTPUT DATA")
print("===========")
print("Spell (Dengan if else) :", __spellIfElse(angka)) 
print("Spell (Dengan switch)  :", __spellMatchCase(angka))