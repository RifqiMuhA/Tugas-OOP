/*	
Nama	     : Rifqi Muhadzib Ahdan - M. Ikhsan Fadhilah - M. Zidan Yohanza - M. Faris Ary Prasetyo
NPM		     : 140810210029 - 140810210003 - 140810210021 -140810190056
Kelas		 : A
Tanggal	     : 19 Oktober 2022
Deskripsi    : Menentukan huruf mutu dan lama durasi ujian masing-masing mahasiswa yang dikumpukan dengan array of class dan mencari nilai tertinggi, terenda, dan rata-rata nilai semua mahasiswa
*/

#include <iostream>
#include <iomanip>

class Waktu{
    private:
        int jam, menit, detik;

    public:
        Waktu(){
            this->jam = 0;
            this->menit = 0;
            this->detik = 0;
        }

        Waktu(int jam, int menit, int detik){
            this->jam = jam;
            this->menit = menit;
            this->detik = detik;
        }

        // Setters
        void setJam(int jam){
            this->jam = jam;
        }
        void setMenit(int menit){
            this->menit = menit;
        }
        void setDetik(int detik){
            this->detik = detik;
        }
        void setWaktu(int jam, int menit, int detik){
            this->jam = jam;
            this->menit = menit;
            this->detik = detik;
        }

        // Getters
        int getJam(){
            return this->jam;
        }
        int getMenit(){
            return this->menit;
        }
        int getDetik(){
            return this->detik;
        }

        Waktu getDurasi(Waktu awal, Waktu akhir){
            int detikAwal = awal.getJam() * 3600 + awal.getMenit() * 60 + awal.getDetik();
            int detikAkhir = akhir.getJam() * 3600 + akhir.getMenit() * 60 + akhir.getDetik();
            int durasi = detikAkhir - detikAwal;

            int jam = durasi / 3600;
            int menit = (durasi % 3600) / 60;
            int detik = (durasi % 3600) % 60;

            return Waktu(jam, menit, detik);
        }

        std::string printWaktu(){
            return std::to_string(this->jam) + ":" + std::to_string(this->menit) + ":" + std::to_string(this->detik);
        }

        bool fixTime(Waktu waktu){
            bool durasiErr;
            int detikMulai = this->jam * 3600 + this->menit * 60 + this->detik;
            int detikSelesai = waktu.getJam() * 3600 + waktu.getMenit() * 60 + waktu.getDetik();

            if (detikMulai > detikSelesai){
                durasiErr = true;
                std::cout << "Waktu selesai harus lebih besar dari waktu mulai" << std::endl;
            } else {
                durasiErr = false;
            }
            return durasiErr;
        }

        Waktu inputWaktu(){
            bool waktuValidation = false;
            int jam, menit, detik;

            do{
                std::cout << "Jam : ";
                std::cin >> jam;

                if(jam < 0 || jam > 23){
                    std::cout << "Waktu tidak valid" << std::endl;
                    continue;
                }

                std::cout << "Menit : ";
                std::cin >> menit;

                if(menit < 0 || menit > 59){
                    std::cout << "Waktu tidak valid" << std::endl;
                    continue;
                }

                std::cout << "Detik : ";
                std::cin >> detik;

                if(detik < 0 || detik > 59){
                    std::cout << "Waktu tidak valid" << std::endl;
                    continue;
                }

                waktuValidation = true;

            } while (!waktuValidation);

            return Waktu(jam, menit, detik);
        }
};

class Mahasiswa
{
private:
    std::string nama, npm;
    Waktu awal, akhir;
    int nilai;

public:
    Mahasiswa(){
        this->nama = "";
        this->npm = "";
        this->nilai = 0;
        this->awal = Waktu(0, 0, 0);
        this->akhir = Waktu(0, 0, 0);
    }

    Mahasiswa(std::string nama, std::string npm, Waktu awal, Waktu akhir, int nilai){
        this->nama = nama;
        this->npm = npm;
        this->awal = awal;
        this->akhir = akhir;
        this->nilai = nilai;
    }

    void setNama(std::string nama){
        this->nama = nama;
    }

    void setNpm(std::string npm){
        this->npm = npm;
    }

    void setAwal(Waktu awal){
        this->awal = awal;
    }

    void setAkhir(Waktu akhir){
        this->akhir = akhir;
    }

    void setNilai(int nilai){
        this->nilai = nilai;
    }

    std::string getNama(){
        return this->nama;
    }

    std::string getNpm(){
        return this->npm;
    }

    Waktu getAwal(){
        return this->awal;
    }

    Waktu getAkhir(){
        return this->akhir;
    }

    int getNilai(){
        return this->nilai;
    }

    Waktu getWaktuDurasi(){
        return this->awal.getDurasi(this->awal, this->akhir);
    }

    char getHurufMutu() {
        if (nilai >= 80 && nilai <= 100){
            return 'A';
        } else if (nilai >= 68 && nilai < 80){
            return 'B';
        } else if (nilai >= 55 && nilai < 68){
            return 'C';
        } else if (nilai >= 45 && nilai < 55){
            return 'D';
        } else if (nilai >= 0 && nilai < 45){
            return 'E';
        } else {
            return ' ';
        }
    }

    int getHighScore(Mahasiswa mhs[], int n){
        int max = 0;
        for (int i = 0; i < n; i++){
            if (mhs[i].getNilai() > max){
                max = mhs[i].getNilai();
            }
        }
        return max;
    }

    int getLowScore(Mahasiswa mhs[], int n){
        int min = 100;
        for (int i = 0; i < n; i++){
            if (mhs[i].getNilai() < min){
                min = mhs[i].getNilai();
            }
        }
        return min;
    }

    double getMeanScore(Mahasiswa mhs[], int n){
        int total = 0;
        for (int i = 0; i < n; i++){
            total += mhs[i].getNilai();
        }
        return total / n;
    }

    std::string kelulusan(){
        if (getNilai() >= 55){
            return "Lulus";
        } else {
            return "Gagal";
        }
    }

    void inputMahasiswa(Mahasiswa mhs[], int n){
        std::string nama, npm;
        Waktu awal = Waktu(0, 0, 0);
        Waktu akhir = Waktu(0, 0, 0);
        int nilai;

        for (int i = 0; i < n; i++){
            std::cout << "\nMahasiswa ke-" << i + 1 << std::endl;
            std::cout << "Nama : ";
            std::cin.ignore();
            std::getline(std::cin, nama);
            std::cout << "NPM : ";
            std::cin >> npm;

            do{
                std::cout << "===Waktu Mulai===" << std::endl;
                awal = awal.inputWaktu();

                std::cout << "===Waktu Selesai===" << std::endl;
                akhir = akhir.inputWaktu();

            } while (awal.fixTime(akhir));
            std::cout << "Nilai : ";
            std::cin >> nilai;

            mhs[i] = Mahasiswa(nama, npm, awal, akhir, nilai);
        }
    }

    void printData(Mahasiswa mhs[], int n)
    {   
        std::cout << "\n============================================= DATA MAHASISWA =================================================================" << std::endl;
        std::cout << std::setw(5) << "No" << std::setw(20) << "Nama" << std::setw(20) << "NPM" << std::setw(15) << "Nilai Ujian" << std::setw(10) << "HM" << std::setw(15) << "Waktu Mulai" << std::setw(15) << "Waktu Selesai" << std::setw(15) << "Waktu Durasi" << std::setw(10) << "Status" << std::endl;
        for (int i = 0; i < n; i++)
        {
            std::cout << std::setw(5) << i + 1 << std::setw(20) << mhs[i].getNama() << std::setw(20) << mhs[i].getNpm() << std::setw(15) << mhs[i].getNilai() << std::setw(10) << mhs[i].getHurufMutu() << std::setw(15) << mhs[i].getAwal().printWaktu() << std::setw(15) << mhs[i].getAkhir().printWaktu() << std::setw(15) << mhs[i].getWaktuDurasi().printWaktu() << std::setw(10) << mhs[i].kelulusan() << std::endl;
        }
        std::cout << "==============================================================================================================================" << std::endl;
        std::cout << "Rata-rata Nilai : " << mhs[0].getMeanScore(mhs, n) << std::endl;
        std::cout << "Nilai Tertinggi: " << mhs[0].getHighScore(mhs, n) << std::endl;
        std::cout << "Nilai Terendah: " << mhs[0].getLowScore(mhs, n) << std::endl;

    }
};

main()
{
    int n;
    std::cout << "Masukkan jumlah mahasiswa : ";
    std::cin >> n;

    Mahasiswa mhs[n];
    mhs->inputMahasiswa(mhs, n);
    mhs->printData(mhs, n);
}