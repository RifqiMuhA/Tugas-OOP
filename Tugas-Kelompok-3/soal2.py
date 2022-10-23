"""
Nama	     : Rifqi Muhadzib Ahdan - M. Ikhsan Fadhilah - M. Zidan Yohanza - M. Faris Ary Prasetyo
NPM		     : 140810210029 - 140810210003 - 140810210021 -140810190056
Kelas		 : A
Tanggal	     : 07 Oktober 2022
Deskripsi	 : Menentukan gaji lembur berdasarkan golongan dan durasi lembur
"""

class Karyawan :
    
    def __init__(self, nama, nip, gol) :
        self.nama = nama
        self.nip = nip
        self.gol = gol
        
    def setNama(self, nama) :
        self.nama = nama
    
    def setNip(self, nip) :
        self.nip = nip
        
    def setGol(self, gol) :
        self.gol = gol
        
    def getNama(self) :
        return self.nama
    
    def getNip(self) :
        return self.nip
        
    def getGol(self) :
        return self.gol
    
    def inputData(self) :
        self.setNip(input("Nip            : "))
        self.setNama(input("Nama           : "))
        self.setGol(input("Golongan       : "))
    
    def gajiPokok(self) :
        if (self.gol == "1") :
            gaPok = 150000
        elif (self.gol == "2") : 
            gaPok = 200000
        elif (self.gol == "3") : 
            gaPok = 400000
        elif (self.gol == "4") : 
            gaPok = 500000
        else :
            gaPok = 0
        return gaPok
    
    def gajiLembur(self, wktAkhir, wktAwal, wktDurasi) :
        waktuLembur = wktAkhir.hitungDurasiLembur(wktAwal, wktDurasi)
        jamLembur = waktuLembur.getHour()
        if (self.gol == "1") :
            gaLem = 50000
        elif (self.gol == "2") :
            gaLem = 70000
        elif (self.gol == "3") :
            gaLem = 150000
        elif (self.gol == "4") :
            gaLem = 200000
        else :
            gaLem = 0
        gaLem *= jamLembur
        return gaLem
    
    def gajiHarian(self, wktAkhir, wktAwal, wktDurasi) :
        return self.gajiPokok() + self.gajiLembur(wktAkhir, wktAwal, wktDurasi)

    def gajiTotal(self, wktAkhir, wktAwal, wktDurasi) :
        total = 0
        total += self.gajiHarian(wktAkhir, wktAwal, wktDurasi)
        
    def printData(self, urutan, wktAwal, wktAkhir, wktLembur) :
        print("{:<5} {:<17} {:<17} {:<6} {:<15} {:<15} {:<18} {:<12} {:<15} {:<21}".format ((urutan), self.nama, self.nip , self.gol, wktAwal.konversiToMilitary() , wktAkhir.konversiToMilitary(), wktAkhir.hitungDurasiKerja(wktAwal, wktLembur).konversiToMilitary() , wktAkhir.hitungDurasiLembur(wktAwal, wktLembur).konversiToMilitary(), self.gajiHarian(wktAkhir, wktAwal, wktLembur), wktAkhir.statusPeringatan(wktAwal)))
    
    
class Time : 
    def __init__(self, hour, minute, second) :
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def setHour(self, hour) :
        self.hour = hour
    
    def setMinute(self, minute) :
        self.minute = minute
        
    def setSecond(self, second) :
        self.second = second
        
    def setTime(self, hour, minute, second) :
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
        
    def setTimeDariMilitary(self, time) :
        self.hour   = int(time[0:2])
        self.minute = int(time[3:5])
        self.second = int(time[6:8])
        
    def inputTime(self, teks) :
        value = input(teks)
        return value
    
    def fixTime(self) :
        if (self.second >= 60) :
            self.minute += (self.second / 60)
            self.second %= 60
        
        if (self.minute >= 60) :
            self.hour += (self.minute / 60)
            self.menit %= 60
        
        if (self.hour >= 24) :
            self.hour %= 24
            
        
    def konversiToDetik(self) :
        return (self.hour*3600 + 
                self.minute*60 + 
                self.second
                )
        
    def konversiToMilitary(self) :
        hour = str(self.hour)
        minute = str(self.minute)
        second = str(self.second)
        return(hour + ":" + minute + ":" + second)
        
    def hitungDurasiKerja(self, wktAwal, wktDurasi) :
        durasi = self.konversiToDetik() - wktAwal.konversiToDetik()
        if(durasi < 0) :
            durasi += (24*3600)
            
        wktDurasi.setTime((durasi/3600), ((durasi%3600)/60), ((durasi%3600)%60))
        
        return wktDurasi
    
    def hitungDurasiLembur(self, wktAwal, wktDurasi) :

        durasi = self.konversiToDetik() - wktAwal.konversiToDetik()
        
        if(durasi < 0) : 
            durasi += (24*3600)
        
        durasiLembur = durasi - (8*3600)
        
        if(durasiLembur < 0) :
            durasiLembur = 0
        
        wktDurasi.setTime((durasiLembur/3600), ((durasiLembur%3600)/60), ((durasiLembur%3600)%60))
        
        return wktDurasi
    
    def statusPeringatan(self, wktAwal) :
        durasi = self.konversiToDetik() - wktAwal.konversiToDetik()
        if(durasi < 0) :
            durasi += (24*3600)
            
        if(durasi >= 0 and durasi < (8*3600)) :
            return "SP1"
        else :
            return "---"
                
    def getHour(self) :
        return self.hour
    
    def getMinute(self) :
        return self.minute
    
    def getSecond(self) :
        return self.second
    
    

size = int(input("Masukkan Banyak Pegawai : "))

employeeArr = []
awalArr = []
akhirArr = []
totalArr = []
wAwalArr = []
wAkhirArr = []


for x in range(0, size):
    employee = Karyawan(0,0,0)
    employeeArr.append(employee)
    awal = Time(0 , 0 , 0)
    awalArr.append(awal)
    akhir = Time(0 , 0 , 0)
    akhirArr.append(akhir)
    total = Time(0 , 0 , 0)
    totalArr.append(total)
    
    print("\nInput data pegawai ke-" , (x + 1))
    employee.inputData()
    awal.setTimeDariMilitary(input("Waktu Datang : "))
    awal.fixTime()
    wAwalArr.append(awal)
    akhir.setTimeDariMilitary(input("Waktu Pulang : "))
    akhir.fixTime()
    wAkhirArr.append(akhir) 
    
    i = 1
    result = 0
    
    print("-----+-----------------+------+---------------+---------------+----------------------------+------------+--------------+---------------------+")
    print ("{:<5} {:<17} {:<17} {:<6} {:<15} {:<15} {:<18} {:<12} {:<15} {:<21}".format('No.', 'NIP','Nama','Gol','Waktu mulai','Waktu selesai','Total Waktu','Jam Lembur','Gaji','Status Peringatan'))
    print("-----+-----------------+------+---------------+---------------+----------------------------+------------+--------------+---------------------+")
    
    for employee, total, awal, akhir in zip(employeeArr, totalArr, wAwalArr, wAkhirArr) :
        
        employee.printData(i, awal, akhir, total)
        i+=1
        result += employee.gajiHarian(akhir, awal, total)
            
    print("-----+-----------------+------+---------------+---------------+----------------------------+------------+--------------+---------------------+")
    print("Total Gaji :" , result)
    
    