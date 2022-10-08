import java.time.LocalTime;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String nip, nama, gol, datang, pulang;
        int n, totalGaji = 0;

        System.out.print("Input jumlah pegawai : ");
        n = input.nextInt();
        input.nextLine();

        Pegawai[] pegawai = new Pegawai[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nData pegawai ke-" + (i + 1) + " : ");
            System.out.print("Input NIP : ");
            nip = input.nextLine();
            System.out.print("Input nama : ");
            nama = input.nextLine();
            System.out.print("Input golongan [1-4] : ");
            gol = input.nextLine();
            System.out.print("Input Waktu datang (hh:mm:ss): ");
            datang = input.nextLine();
            System.out.print("Input Waktu pulang (hh:mm:ss): ");
            pulang = input.nextLine();

            LocalTime datangTime = LocalTime.parse(datang);
            LocalTime pulangTime = LocalTime.parse(pulang);

            pegawai[i] = new Pegawai(nip, nama, gol, datangTime, pulangTime);
        }

        System.out.println("\n\t\tDaftar Gaji Harian PT Informatika");
        System.out.println(
                "--------------------------------------------------------------------------------------------------");
        System.out.println("No.\tNIP\tNama\tGol\tDatang\tPulang\tLama\tJam Lembur\tGaji Harian\tStatus");
        System.out.println(
                "--------------------------------------------------------------------------------------------------");
        for (int i = 0; i < pegawai.length; i++) {

            System.out.print((i + 1) + "\t" + pegawai[i].getNip() + "\t" + pegawai[i].getNama() + "\t"
                    + pegawai[i].getGol() + "\t" + pegawai[i].getDatang().toString() + "\t"
                    + pegawai[i].getPulang().toString() + "\t"
                    + pegawai[i].getLamaKerja().toString() + "\t" + pegawai[i].getJamLembur().toString() + "\t\t"
                    + pegawai[i].getGajiHarian()
                    + "\t\t");
            if (pegawai[i].getPeringatan()) {
                System.out.println("SP1");
            } else {
                System.out.println("---");
            }
            totalGaji += pegawai[i].getGajiHarian();
        }
        System.out.println(
                "--------------------------------------------------------------------------------------------------");
        System.out.println("Total Gaji : " + totalGaji);
    }
}
