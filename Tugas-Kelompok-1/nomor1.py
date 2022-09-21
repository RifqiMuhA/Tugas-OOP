""" Nama program : nomor1.py
    Nama         : Mohammad Faris Arie Prasetyo, Muhammad Ikhsan Fadhilah, Mohammad Zidan Yohanza, Rifqi Muhadzib Ahdan
    NPM          : 140810190056, 140810210003, 140810210021, 140810210029
    Tanggal buat : 18 September 2022
    Deskripsi    : Huruf Mutu
******************************************************"""
    
# Fungsi Memasukkan String  
def inputString(message) :
    word = input(message)
    return word
    
# Fungsi Memasukkan angka float   
def inputFloat(message) :
    value = float(input(message))
    return value
    
# Fungsi Menentukan Huruf Mutu   
def hurufMutu(mean) :
    if(mean >= 80 and mean <= 100) :
        mutu = 'A'
    elif(mean >= 68 and mean < 80) :
        mutu = 'B'
    elif(mean >= 55 and mean < 68) :
        mutu = 'C'
    elif(mean >= 45 and mean < 55) :
        mutu = 'D'
    else :
        mutu = 'E'
    return mutu
    
# Fungsi Status Mutu   
def Status(mean) :
        if(mean >= 55 and mean <= 100) :
            stat = "Lulus"
        else :
            stat = "Tidak Lulus"
        
        return stat
    
# Fungsi Output      
def outputMutu(mutu, mean, status, name, npm) :
    print("Nama       : " , name)
    print("NPM        : " , npm)
    print("Huruf Mutu : " , mutu)
    print("Rata-rata  : " , mean)
    print("Keterangan : " , status)
    
# main program
name = inputString("Masukkan Nama          : ")
npm  = inputString("Masukkan NPM           : ")
Skor1 = inputFloat("Masukkan Nilai Pertama : ")
Skor2 = inputFloat("Masukkan Nilai Kedua   : ")
Skor3 = inputFloat("Masukkan Nilai Ketiga  : ")
print()
        
mean = (Skor1+Skor2+Skor3)/3
hMutu = hurufMutu(mean)
stat = Status(mean)
outputMutu(hMutu, mean, stat, name, npm)
