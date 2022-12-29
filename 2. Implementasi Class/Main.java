public class Main{
    public static void main(String[] args){
        BangunRuang bangunruang = new BangunRuang();
        bangunruang.volume();
        bangunruang.keliling();

        System.out.println("+++++++++++++++++++++++++++++++++");

        Balok balok = new Balok();
        balok.panjang = 12;
        balok.lebar = 10;
        balok.tinggi = 8;
        balok.hasilkeliling();
        balok.hasilvolume();
        
        Kubus kubus = new Kubus();
        kubus.sisi = 5;
        kubus.hasilkeliling();
        kubus.hasilvolume();
        
        Tabung tabung = new Tabung();
        tabung.tinggi = 9;
        tabung.jarijari = 4;
        tabung.hasilkeliling();
        tabung.hasilvolume();
    }
}