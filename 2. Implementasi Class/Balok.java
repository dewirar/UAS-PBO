public class Balok extends BangunRuang {
    float panjang;
    float lebar;
    float tinggi;
    
    float hasilkeliling(){
        keliling = 4 * (panjang+lebar+tinggi);
        System.out.println("Keliling Balok : "+keliling);
        return 0;
    }

    float hasilvolume(){
        volume = panjang * lebar * tinggi;
        System.out.println("Volume Balok : "+volume);
        return 0;
    }
}
