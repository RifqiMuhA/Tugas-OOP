import java.time.LocalTime;

public class Pegawai {

    private String nip, nama, gol;
    LocalTime datang, pulang;

    public Pegawai(String nip, String nama, String gol, LocalTime datang, LocalTime pulang) {
        this.nip = nip;
        this.nama = nama;
        this.gol = gol;
        this.datang = datang;
        this.pulang = pulang;
    }
    

    public String getNip() {
        return this.nip;
    }

    public void setNip(String nip) {
        this.nip = nip;
    }

    public String getNama() {
        return this.nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public String getGol() {
        return this.gol;
    }

    public void setGol(String gol) {
        this.gol = gol;
    }

    public LocalTime getDatang() {
        return this.datang;
    }

    public void setDatang(LocalTime datang) {
        this.datang = datang;
    }

    public LocalTime getPulang() {
        return this.pulang;
    }

    public void setPulang(LocalTime pulang) {
        this.pulang = pulang;
    }

    public int getGapok() {
        int gapok = 0;
        switch (this.gol) {
            case "1":
                gapok = 150000;
                break;
            case "2":
                gapok = 200000;
                break;
            case "3":
                gapok = 400000;
                break;
            case "4":
                gapok = 500000;
                break;
        }
        return gapok;
    }

    public LocalTime getLamaKerja() {
        int lamaDetik = this.pulang.toSecondOfDay() - this.datang.toSecondOfDay();

        int jam = lamaDetik / 3600;
        int menit = (lamaDetik % 3600) / 60;
        int detik = (lamaDetik % 3600) % 60;

        return LocalTime.of(jam, menit, detik);
    }

    public boolean getPeringatan() {
        if (getLamaKerja().getHour() < 8)
            return true;
        else
            return false;
    }

    public int getGajiLembur() {
        int lembur = 0;
        switch (this.gol) {
            case "1":
                lembur = 50000;
                break;
            case "2":
                lembur = 70000;
                break;
            case "3":
                lembur = 150000;
                break;
            case "4":
                lembur = 200000;
                break;
        }
        return lembur;
    }

    public LocalTime getJamLembur() {
        int lamaDetik = getLamaKerja().toSecondOfDay() - (8 * 3600);

        if (lamaDetik < 1) {
            return LocalTime.of(0, 0,0);
        }

        int jam = lamaDetik / 3600;
        int menit = (lamaDetik % 3600) / 60;
        int detik = (lamaDetik % 3600) % 60;

        return LocalTime.of(jam, menit, detik);
    }

    public int getGajiHarian() {
        int lembur = 0;
        if (!getPeringatan())
            lembur = getJamLembur().getHour();
        return this.getGapok() + lembur * getGajiLembur();
    }
}