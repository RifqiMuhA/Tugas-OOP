
/*	
*  Nama	         : Rifqi Muhadzib Ahdan - M. Ikhsan Fadhilah - M. Zidan Yohanza - M. Faris Ary Prasetyo
*  NPM		     : 140810210029 - 140810210003 - 140810210021 -140810190056
*  Kelas		 : A
*  Tanggal	     : 07 Oktober 2022
*  Deskripsi     : Menentukan huruf mutu dan lama durasi ujian masing-masing mahasiswa yang dikumpukan dengan array of class
                   Dan mencari nilai tertinggi, terenda, dan rata-rata nilai semua mahasiswa
**/
import java.util.Scanner;

public class Ujian {
    public static void main(String[] args) {
        Mahasiswa[] ikhsan = new Mahasiswa[10];

        int jumlah = inputInt("Masukkan jumlah mahasiswa : ");

        System.out.println("===INPUT===");
        for (int i = 0; i < jumlah; i++) {
            ikhsan[i] = new Mahasiswa();
            System.out.println("Mahasiswa ke-" + (i+1));
            ikhsan[i] = input();
        }

        System.out.println("===OUTPUT===");
        System.out.format("%-10s%-13s%-15s%-20s%-10s%-15s%-10s%-10s%-10s\n", 
                          "NO",
                          "NAMA", 
                          "NPM", 
                          "NILAI UJIAN",
                          "HM", 
                          "STATUS", 
                          "MULAI", 
                          "SELESAI", 
                          "LAMA"
                        );
        for(int j = 0; j <= 110; j++){
            System.out.print("=");
        }
        for (int i = 0; i < jumlah; i++) {
            output(ikhsan[i], (i+1));
        }
        System.out.println("\nNilai Tertinggi : " + highScore(ikhsan, jumlah));
        System.out.println("Nilai Terendah  : " + lowScore(ikhsan, jumlah));
        System.out.println("Rata-rata nilai : " + meanScore(ikhsan, jumlah));
    }

    static Mahasiswa input() {
        Mahasiswa mhs = new Mahasiswa();

        mhs.setNama(inputString("Nama          : "));
        mhs.setNpm(inputString("NPM           : "));
        mhs.setNilai(inputFloatNilai("Nilai         : "));
        mhs.getAwal().setWaktu(inputString("Waktu Mulai   : "));
        mhs.getAwal().fixTime();
        mhs.getAkhir().setWaktu(inputString("Waktu Selesai : "));
        mhs.getAkhir().fixTime();

        return mhs;
    }

    static void output(Mahasiswa mhs, int urutan) {
        mhs.printAtribut(urutan);
    }

    static String inputString(String pesan) {
        Scanner in = new Scanner(System.in);
        System.out.print(pesan);
        String str = in.nextLine();
        return str;
    }

    static int inputInt(String pesan) {
        Scanner in = new Scanner(System.in);
        System.out.print(pesan);
        int integer = in.nextInt();
        return integer;
    }

    static float inputFloatNilai(String pesan) {
        Scanner in = new Scanner(System.in);
        float nilai = 0f;
        do {
            System.out.print(pesan);
            nilai = in.nextFloat();
        } while (cekRange(nilai));
        return nilai;
    }

    static boolean cekRange(float nilai) {
        if (nilai >= 0 && nilai <= 100) {
            return false;
        } else {
            System.out.println("Silakan input nilai sesuai range");
            return true;
        }
    }

    static float meanScore(Mahasiswa[] mhs, int jumlah) {
        float result = 0;
        for (int i = 0; i < jumlah; i++) {
            result += mhs[i].getNilai() ;
        }
        return (result / (float)jumlah);
    }

    static float highScore(Mahasiswa[] mhs, int jumlah) {
        int i = 1;
        float maks = mhs[0].getNilai();
        while (i < jumlah) {
            if (mhs[i].getNilai() > maks) {
                maks = mhs[i].getNilai();
            }
            i++;
        }
        return maks;
    }

    static float lowScore(Mahasiswa[] mhs, int jumlah) {
        int i = 1;
        float min = mhs[0].getNilai();
        while (i < jumlah) {
            if (mhs[i].getNilai() < min) {
                min = mhs[i].getNilai();
            }
            i++;
        }
        return min;
    }

}

class Mahasiswa {
    private String nama, npm;
    private float nilai;
    private Waktu awal, akhir;

    // Constructors
    public Mahasiswa() {
        this.nama = null;
        this.npm = null;
        this.nilai = 0f;
        awal = new Waktu();
        akhir = new Waktu();
    }

    // Setters
    public void setNama(String nama) {
        this.nama = nama;
    }

    public void setNpm(String npm) {
        this.npm = npm;
    }

    public void setNilai(float nilai) {
        this.nilai = nilai;
    }

    public void setAwal(Waktu awal) {
        this.awal = awal;
    }

    public void setAkhir(Waktu akhir) {
        this.akhir = akhir;
    }

    // Getters
    public String getNama() {
        return this.nama;
    }

    public String getNpm() {
        return this.npm;
    }

    public float getNilai() {
        return this.nilai;
    }

    public Waktu getAwal() {
        return this.awal;
    }

    public Waktu getAkhir() {
        return this.akhir;
    }

    public char hurufMutu() {
        if (this.nilai >= 0 && this.nilai < 45) {
            return 'E';
        } else if (this.nilai >= 45 && this.nilai < 55) {
            return 'D';
        } else if (this.nilai >= 55 && this.nilai < 68) {
            return 'C';
        } else if (this.nilai >= 68 && this.nilai < 80) {
            return 'B';
        } else {
            return 'A';
        }
    }

    public String kelulusan() {
        return (this.nilai >= 55) ? "Lulus" : "Tidak Lulus";
    }

    public void printAtribut(int urutan) {
        Waktu waktuDurasi = new Waktu();

        System.out.format("\n%-10d", urutan);
        System.out.format("%-13s", this.nama);
        System.out.format("%-15s", this.npm);
        System.out.format("%-20f", this.nilai);
        System.out.format("%-10c", hurufMutu());
        System.out.format("%-15s", kelulusan());
        System.out.format("%-10s", this.awal.printWaktu()); 
        System.out.format("%-10s", this.akhir.printWaktu()); 
        // Passing object cara 1 (void)
        waktuDurasi.hitungDurasi(this.awal, this.akhir);
        waktuDurasi.fixTime();
        System.out.format("%-10s", waktuDurasi.printWaktu()); 
    }
}

class Waktu {
    private int jam, menit, detik;

    // Constructor
    public Waktu() {
        this.jam = 0;
        this.menit = 0;
        this.detik = 0;
    }

    // Setters
    public void setJam(int jam) {
        this.jam = jam;
    }

    public void setMenit(int menit) {
        this.menit = menit;
    }

    public void setDetik(int detik) {
        this.detik = detik;
    }

    public void setWaktu(String waktu) {
        String[] arrWaktu = waktu.split(":");
        this.jam = Integer.parseInt(arrWaktu[0]);
        this.menit = Integer.parseInt(arrWaktu[1]);
        this.detik = Integer.parseInt(arrWaktu[2]);
    }

    // Getters
    public int getJam() {
        return this.jam;
    }

    public int getMenit() {
        return this.menit;
    }

    public int getDetik() {
        return this.detik;
    }

    public void fixTime() {
        if (this.detik >= 60) {
            this.menit += (this.detik / 60);
            this.detik %= 60;
        }
        if (this.menit >= 60) {
            this.jam += (this.menit / 60);
            this.menit %= 60;
        }
        if (this.jam >= 24) {
            this.jam %= 24;
        }
    }

    // Passing object cara 1 (void)
    public void hitungDurasi(Waktu awal, Waktu akhir) {
        this.detik += (akhir.getDetik() - awal.getDetik());
        if (this.detik < 0) {
            this.menit -= 1;
            this.detik += 60;
        }

        this.menit += (akhir.getMenit() - awal.getMenit());
        if (this.menit < 0) {
            this.jam -= 1;
            this.menit += 60;
        }

        this.jam += (akhir.getJam() - awal.getJam());
        if (this.jam < 0) {
            this.jam += 24;
        }
    }

    public String printWaktu() {
        return String.format("%02d:%02d:%02d", this.jam, this.menit, this.detik);
    }
}
