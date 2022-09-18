""" Nama program : nomo3.py
    Nama         : Mohammad Faris Arie Prasetyo, Muhammad Ikhsan Fadhilah, Mohammad Zidan Yohanza, Rifqi Muhadzib Ahdan
    NPM          : 140810190056, 140810210003, 140810210021, 140810210029
    Tanggal buat : 18 September 2022
    Deskripsi    : Gaji Pegawai
******************************************************"""

# Fungsi Input String 
def inputString() :
    word = input("Masukkan Nama Anda : ")
    return word

# Fungsi Input Integer
def inputInteger() :
    value = int(input("Masukkan Golongan : "))
    return value

# Fungsi Operasi Gaji Total
def gajiTotal(name, gol) :
    match gol :
        case 1 :
            gapok = 1500000
            potongan = gapok*(1*0.01)
            tunjangan = gapok*(10*0.01)
            gatot = gapok + tunjangan - potongan
            outputData(name, gol, gapok, tunjangan, potongan, gatot)
        
        case 2 :
            gapok = 2000000
            potongan = gapok*(2*0.01)
            tunjangan = gapok*(12*0.01)
            gatot = gapok + tunjangan - potongan
            outputData(name, gol, gapok, tunjangan, potongan, gatot)
            
        case 3 :
            gapok = 3000000
            potongan = gapok*(2*0.01)
            tunjangan = gapok*(12*0.01)
            gatot = gapok + tunjangan - potongan
            outputData(name, gol, gapok, tunjangan, potongan, gatot)
            
        case 4 :
            gapok = 5000000
            potongan = gapok*(4*0.01)
            tunjangan = gapok*(15*0.01)
            gatot = gapok + tunjangan - potongan
            outputData(name, gol, gapok, tunjangan, potongan, gatot)

# Fungsi Output         
def outputData(name, gol, gapok, tunjangan, potongan, gatot) :
    print("Nama Pegawai : " , name)
    print("Golongan     : " , gol)
    print("Gaji Pokok   : " , gapok)
    print("Tunjangan    : " , round(tunjangan))
    print("Potongan     : " , round(potongan))
    print("Gaji Total   : " , round(gatot))
   
# main program 
name = inputString()
gol = inputInteger()

print()
gajiTotal(name, gol)