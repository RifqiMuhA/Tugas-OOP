""" Nama program : nomo3.py
    Nama         : Mohammad Faris Arie Prasetyo, Muhammad Ikhsan Fadhilah, Mohammad Zidan Yohanza, Rifqi Muhadzib Ahdan
    NPM          : 140810190056, 140810210003, 140810210021, 140810210029
    Tanggal buat : 18 September 2022
    Deskripsi    : Gaji Pegawai
******************************************************"""

# Fungsi Input Nama
def inputString() :
    word = input("Masukkan Nama Anda : ")
    return word

def status(bil) :
    if (bil >= 1 and bil <= 4) :
        return 0
    else :
        return 1  

# Fungsi Input Integer
def inputInteger() :
    stat = 1
    while(stat) :
        value = int(input("Masukkan Golongan 1-4 : "))
        stat = status(value)
    return value

# Fungsi Operasi Gaji Pokok
def gajiPokok(gol) :
    match gol :
        case 1 :
            gapok = 1500000
        
        case 2 :
            gapok = 2000000
            
        case 3 :
            gapok = 3000000
            
        case 4 :
            gapok = 5000000
    return gapok

# Fungsi Operasi Potongan
def potonganGaji(gol) :
    match gol :
        case 1 :
            potongan = 0.01
        
        case 2 :
            potongan = 0.02
            
        case 3 :
            potongan = 0.02
            
        case 4 :
            potongan = 0.04
    return (potongan * gajiPokok(gol))

# Fungsi Operasi Tunjangan 
def tunjanganGaji(gol) :
    match gol :
        case 1 :
            tunjangan = 0.01
        
        case 2 :
            tunjangan = 0.12
            
        case 3 :
            tunjangan = 0.12
            
        case 4 :
            tunjangan = 0.15
    return (tunjangan * gajiPokok(gol))

# Fungsi Operasi Gaji Total
def gajTot(gapok, potongan, tunjangan) :
    return (gapok + tunjangan - potongan)

# Fungsi Output         
def outputData(name, gol, gapok, tunjangan, potongan, gatot) :
    print("~~~~~~~OUTPUT DATA~~~~~~~")
    print("Nama Pegawai :" , name)
    print("Golongan     :" , gol)
    print("Gaji Pokok   : Rp" , gapok)
    print("Tunjangan    : Rp" , round(tunjangan))
    print("Potongan     : Rp" , round(potongan))
    print("Gaji Total   : Rp" , round(gatot))
    print()
   
# main program 
print("~~~~~~~INPUT DATA~~~~~~~")
name = inputString()
gol = inputInteger()
gajpok = gajiPokok(gol)
potongan = potonganGaji(gol)
tunjangan = tunjanganGaji(gol)
gatot = gajTot(gajpok, potongan, tunjangan)

print()
outputData(name, gol, gajpok, tunjangan, potongan, gatot)