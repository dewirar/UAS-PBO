public class Tabung extends BangunRuang{
    float jarijari;
    float tinggi;
    
    float hasilkeliling(){
        keliling = 2.14*2*jarijari;
        System.out.println("Keliling Tabung : "+keliling);
        return 0;
    }

    float hasilvolume(){
        volume = (2.14 * jarijari * jarijari) * tinggi;
        System.out.println("Volume Tabung : "+volume);
        return 0;
    }
}
