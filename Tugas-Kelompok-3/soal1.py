#  Nama	         : Rifqi Muhadzib Ahdan - M. Ikhsan Fadhilah - M. Zidan Yohanza - M. Faris Ary Prasetyo
#  NPM		     : 140810210029 - 140810210003 - 140810210021 -140810190056
#  Kelas		 : A
#  Tanggal	     : 19 Oktober 2022
#  Deskripsi     : Menentukan huruf mutu dan lama durasi ujian masing-masing mahasiswa yang dikumpukan dengan array of object
#                  Serta mencari nilai tertinggi, terendah, dan rata-rata nilai semua mahasiswa

class daftarMahasiswa :
    def __init__(self, jumlah=0):
        self.__jumlah = jumlah
        self.__arrMahasiswa = []
     # Setters
    def setJumlah(self, jumlah):
        self.__jumlah = jumlah
    def isiArr(self):
        for i in range(0, self.__jumlah) :
            tempMahasiswa = Mahasiswa()
            print("Mahasiswa ke-" + str((i)+1))
            tempMahasiswa.inputMahasiswa()
            self.__arrMahasiswa.append(tempMahasiswa)
    def printDaftar(self):
        totalNilai = 0
        max = 0
        min = 100

        print("===OUTPUT===")
        print("\t\t\t\t\tDaftar Nilai Ujian dan Lama Ujian\n\n")
        print("{:<5s} {:<13s} {:<15s} {:<20s} {:<10s} {:<15s} {:<10s} {:<10s} {:<10s}".format("NO", "NAMA", "NPM", "NILAI UJIAN", "HM", "STATUS", "MULAI", "SELESAI", "LAMA"))
        for x in range(0, 120):
            print("=", end='')
        print()
        for i in range(0, self.__jumlah):
            # Proses cari max, min, dan rerata
            temp = self.__arrMahasiswa[i]
            if(temp.getNilai() > max): max = temp.getNilai()
            if(temp.getNilai() < min): min = temp.getNilai()
            totalNilai += temp.getNilai()

            # Row per mahasiswa
            temp.toTableRow((i+1))
        print("\nNilai Tertinggi : ", max)
        print("Nilai Terendah  : ", min)
        print("Rata-rata nilai : ", (totalNilai/self.__jumlah))

class Mahasiswa :
    # Constructors
    def __init__(self, nama=None, npm=None, nilai=0) :
        self.__nama = nama
        self.__npm = npm
        self.__nilai = nilai
        self.__awal = Waktu()
        self.__akhir = Waktu()

    # Setters
    def setNama(self, nama) :
        self.__nama = nama
    def setNpm(self, npm) :
        self.__npm = npm
    def setNilai(self, nilai) :
        self.__nilai = nilai
    def setAwal(self, awal) :
        self.__awal = awal
    def setAkhir(self, akhir) :
        self.__akhir = akhir

    # Getters
    def getNama(self) :
        return self.__nama
    def getNpm(self) :
        return self.__npm
    def getNilai(self) :
        return self.__nilai
    def getAwal(self) :
        return self.__awal
    def getAkhir(self) :
        return self.__akhir
    
    # fungsional
    def inputMahasiswa(self):
        self.setNama(input("Nama          : "))
        self.setNpm(input("NPM           : "))
        self.setNilai(int(input("Nilai         : ")))
        self.getAwal().setWaktuDariMilitary(input("Waktu Mulai   : "))
        self.getAwal().fixTime()
        self.getAkhir().setWaktuDariMilitary(input("Waktu Selesai : "))
        self.getAkhir().fixTime()
    def hurufMutu(self) :
        if (self.__nilai >= 0 and self.__nilai < 45) :
            return 'E'
        elif (self.__nilai >= 45 and self.__nilai < 55) :
            return 'D'
        elif (self.__nilai >= 55 and self.__nilai < 68) :
            return 'C'
        elif (self.__nilai >= 68 and self.__nilai < 80) :
            return 'B'
        else :
            return 'A'
    def kelulusan(self) :
        if(self.__nilai >= 55): return "Lulus"
        else : return "Tidak Lulus"
    def toTableRow(self, urutan) :
        waktuDurasi = Waktu()
        # Passing object cara 1 (without return value)
        waktuDurasi.hitungDurasi(self.__awal, self.__akhir)
        waktuDurasi.fixTime()

        print("{:<5d} {:<13s} {:<15s} {:<20d} {:<10s} {:<15s} {:<10s} {:<10s} {:<10s}"
                .format(urutan, self.__nama, self.__npm, self.__nilai, self.hurufMutu(), 
                self.kelulusan(), self.__awal.printWaktu(), self.__akhir.printWaktu(), 
                waktuDurasi.printWaktu()))

class Waktu:
    # Constructor
    def __init__(self, jam=0, menit=0, detik=0):
        self.__jam = jam
        self.__menit = menit
        self.__detik = detik
    # Setters
    def setJam(self, jam):
        self.__jam = jam
    def setMenit(self, menit):
        self.__menit = menit
    def setDetik(self, detik):
        self.__detik = detik
    def setWaktuDariMilitary(self, waktu):
        arrWaktu = waktu.split(":")
        self.__jam = int(arrWaktu[0])
        self.__menit = int(arrWaktu[1])
        self.__detik = int(arrWaktu[2])
    # Getters
    def getJam(self):
        return self.__jam
    def getMenit(self):
        return self.__menit
    def getDetik(self):
        return self.__detik
    # Fungsi
    def fixTime(self) :
        if (self.__detik >= 60) :
            self.__menit += (self.__detik / 60)
            self.__detik %= 60
        
        if (self.__menit >= 60) :
            self.__jam += (self.__menit / 60)
            self.__menit %= 60
        
        if (self.__jam >= 24) :
            self.__jam %= 24
    # Passing object cara 1 
    def hitungDurasi(self, awal, akhir) :
        self.__detik += (akhir.getDetik() - awal.getDetik())
        if (self.__detik < 0) :
            self.__menit -= 1
            self.__detik += 60

        self.__menit += (akhir.getMenit() - awal.getMenit())
        if (self.__menit < 0) :
            self.__jam -= 1
            self.__menit += 60

        self.__jam += (akhir.getJam() - awal.getJam())
        if (self.__jam < 0) :
            self.__jam += 24 
    def printWaktu(self) :
        return format("%02d:%02d:%02d" %(self.__jam, self.__menit, self.__detik))
    
# main
mhs = daftarMahasiswa()
mhs.setJumlah(int(input("Input jumlah mahasiswa : ")))
mhs.isiArr()
mhs.printDaftar()