/*	
*  Nama	        : Rifqi Muhadzib Ahdan - M. Ikhsan Fadhilah - M. Zidan Yohanza - M. Faris Ary Prasetyo
*  NPM		    : 140810210029 - 140810210003 - 140810210021 -140810190056
*  Kelas		: A
*  Tanggal	    : 19 Oktober 2022
*  Deskripsi	: Menentukan gaji lembur berdasarkan golongan dan durasi lembur masing-masing karyawan
**/

#include <iostream>
#include <iomanip> 

using namespace std;

class Waktu{
  private :
    int jam, menit, detik;

  public:
  // Constructor
  Waktu(){
    this->jam = 0;
    this->menit = 0;
    this->detik = 0;
  }

  // Setters
  void setJam(int jam) {
    this->jam = jam;
  }
  
  void setMenit(int menit) {
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

  void setWaktuDariMilitary(string waktu){ 
    this->jam = stoi(waktu.substr(0,2));
    this->menit = stoi(waktu.substr(3,5));
    this->detik = stoi(waktu.substr(6,8));
    }
    
    // Getters
    int getJam() {
        return this->jam;
    }
    int getMenit() { 
        return this->menit;
    }
    int getDetik() {
        return this->detik;
    }

    // Memverifikasi jam < 24, menit < 60, dan detik < 60
    void fixTime() {
      if (this->detik >= 60) {
        this->menit += (this->detik / 60);
        this->detik %= 60;
      }
      if (this->menit >= 60) {
        this->jam += (this->menit / 60);
        this->menit %= 60;
      }
      if (this->jam >= 24) {
        this->jam %= 24;
        }
    }

    int konversiToDetik(){
        return (this->jam*3600 + 
                this->menit*60 + 
                this->detik
                );
    }

    string konversiToMilitary(){
        return (to_string(this->jam) + ":" + to_string(this->menit) + ":" + to_string(this->detik));
    }

    Waktu hitungDurasiKerja(Waktu wktAwal){
        Waktu waktuDurasi = Waktu();
        int durasi = konversiToDetik() - wktAwal.konversiToDetik();
        // Jika waktu akhir < waktu awal, maka artinya sudah berganti hari
        // Sehingga durasi akan bernilai negatif dan durasi akan ditambah dengan waktu 1 hari (dalam satuan detik)
        if(durasi < 0){
            durasi += (24*3600);
        }
        waktuDurasi.setWaktu((durasi/3600), ((durasi%3600)/60), ((durasi%3600)%60));

        return waktuDurasi;
    }

    // Passing objek cara 2 : passing with return value function
    Waktu hitungDurasiLembur(Waktu wktAwal){
      Waktu waktuDurasi = Waktu();
      int durasiLembur = konversiToDetik() - wktAwal.konversiToDetik();
      // Jika waktu akhir < waktu awal, maka artinya sudah berganti hari
      // Sehingga durasi akan bernilai negatif dan durasi akan ditambah dengan waktu 1 hari (dalam satuan detik)
      if(durasiLembur < 0){ 
        durasiLembur += (24*3600);
      }
      durasiLembur -= (8*3600);
      // Setelah dikurang, jika ternyata niali durasi lembur negatif (yang menandakan bahwa pegawai tidak lembur)
      // Maka nilai durasi lemburnya 0
      if(durasiLembur < 0){
        durasiLembur = 0;
      }
      waktuDurasi.setWaktu((durasiLembur/3600), ((durasiLembur%3600)/60), ((durasiLembur%3600)%60));            
      return waktuDurasi;
    }

    // Passing objek cara 2 : passing with return value function
    string statusPeringatan(Waktu wktAwal){
      int durasi = konversiToDetik() - wktAwal.konversiToDetik();
      if(durasi < 0){
        durasi += (24*3600);
      }
      if(durasi >= 0 && durasi < (8*3600)){
        return "SP1";
      } else {
        return "---";
      }
    }
};

class Karyawan{
  private: 
    string nip, nama;
    int gol;
    Waktu awal, akhir;

  public:
    // Constructor
    Karyawan() {
      this->nama = "-";
      this->nip = "-";
      this->gol = 0;
      this->awal = Waktu();
      this->akhir = Waktu();
    }
    // Setters
    void setNip(string nip){
      this->nip = nip;
    }
    void setNama(string nama) {
      this->nama = nama;
    }
    void setGol(int gol) {
      this->gol = gol;
    }
    // Getters
    string getNip(){
      return this->nip;
    }
    string getNama() {
      return this->nama;
    }
    int getGol() {
      return this->gol;
    }
    Waktu getAwal(){
      return this->awal;
    }
    Waktu getAkhir(){
      return this->akhir;
    }

    int gajiPokok(){
      int gaPok = 0;
      switch(this->gol){
        case 1:
          gaPok = 150000;
          break;
        case 2:
          gaPok = 200000;
          break;
        case 3:
          gaPok = 400000;
          break;
        case 4:
          gaPok = 500000;
          break;
       }
        return gaPok;
    }

    int gajiLembur(){
      int gaLem = 0, jamLembur;
      Waktu waktuLembur = this->akhir.hitungDurasiLembur(awal);
      jamLembur = waktuLembur.getJam();

      switch(this->gol){
        case 1:
          gaLem = 50000;
        break;
        case 2:
                gaLem = 70000;
                break;
            case 3:
                gaLem = 150000;
                break;
            case 4:
                gaLem = 200000;
                break;
        }
        gaLem *= jamLembur;
        return gaLem;
    }

    int gajiHarian(){
      return gajiPokok()+gajiLembur();
    }

    void print(int urutan){
        cout<<  urutan << setw(8);
        cout<< this->nip << setw(13);
        cout<< this->nama << setw(20);
        cout<< this->gol << setw(20);
        cout<< this->awal.konversiToMilitary() << setw(15);
        cout<< this->akhir.konversiToMilitary() << setw(20);
        cout<< this->akhir.hitungDurasiKerja(this->awal).konversiToMilitary() << setw(15); 
        cout<< this->akhir.hitungDurasiLembur(this->awal).konversiToMilitary() << setw(12); 
        cout<< gajiHarian()<< setw(12);
        cout<< this->akhir.statusPeringatan(this->awal) << endl;
    }

    void inputKaryawan() {
      this->setNip(inputstring("Nip            : "));
      this->setNama(inputstring("Nama           : "));
      this->setGol(inputIntGol("Golongan       : "));
      this->awal.setWaktuDariMilitary(inputstring("Waktu Datang   : "));
      this->awal.fixTime();
      this->akhir.setWaktuDariMilitary(inputstring("Waktu Selesai  : "));
      this->akhir.fixTime();
      cout << endl;
    }

    string inputstring(string pesan){  
      string teks;
      cout << pesan;
      cin >> teks;
      return teks;
    }

    int inputInt(string pesan){  
      int value;
      cout << pesan;
      cin >> value;
      return value;
    }

    int inputIntGol(string pesan){
      int gol = 0;
      do {
        cout << pesan;
        cin >> gol;
      } while (cekRange(gol));
      return gol;
    }

    bool cekRange(int gol){
      if (gol >= 1 && gol <= 4){
        return false; 
      } else {
        cout << ("Silakan input golongan sesuai range");
        return true;  
      } 
    }
};


class daftarKaryawan {
  private:
    int jumlah;
    Karyawan worker[100];

  public:
    // Setter
    void setJumlah(int jumlah){
      this->jumlah = jumlah;
    }
    // Getter
    int getJumlah(){
      return this->jumlah;
    } 
    // Fungsional
    void isiDaftar(){
      cout << ("===INPUT===\n");
      for (int i = 0; i < this->jumlah; i++) {
        this->worker[i] = Karyawan();
        cout << ("Karyawan ke-" + to_string(i+1)) << endl;
        this->worker[i].inputKaryawan();
      } 
    }
    void printDaftar(){
      int total = 0;
      cout << ("\n===OUTPUT===\n");
      cout << ("\t\t\t\t\t\t\tDaftar Gaji Harian PT Informatika\n");
      printf("%-8s%-13s%-20s%-15s%-15s%-15s%-15s%-15s%-15s%-10s\n", 
                              "NO",
                              "NIP", 
                              "NAMA", 
                              "GOLONGAN",
                              "DATANG", 
                              "PULANG", 
                              "DURASI KERJA", 
                              "DURASI LEMBUR", 
                              "GAJI HARIAN",
                              "STATUS"
                            );
      for (int i = 0; i < 150; i++) {
        cout << ("=");
      }
      cout << endl;
      for (int i = 0; i < this->jumlah; i++) {
        worker[i].print((i+1));
        total += worker[i].gajiHarian();
      }
      cout << ("-----+-----------------+-----------+---------------+-------------------+----------------------------+------------+--------------+---------------------+\n");
      cout << "Total Gaji :" << total;
    }
};   

int main(){
    daftarKaryawan list;
    Karyawan employee;
    list.setJumlah(employee.inputInt("Masukkan Jumlah Karyawan : "));

    list.isiDaftar();
    list.printDaftar();

}
