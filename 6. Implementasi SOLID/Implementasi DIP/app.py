from barang_elektronik import BarangElektronik
from kipas_angin import KipasAngin
from lampu import Lampu
from saklar import Saklar


class App:
    
    def __init__(self, saklar: Saklar, barang_elektronik: BarangElektronik):
        self.__saklar = saklar
        self.__barang_elektronik = barang_elektronik
    
    def start(self):
        self.__saklar.berubah(self.__perubahan)
        

if __name__ == '__main__':
    
    lampu = Lampu()
    kipas_angin = KipasAngin()
    saklar = Saklar()
    
    app_lampu = App(saklar, lampu)
    app_lampu.start()
    
    app_kipas_angin = App(saklar, kipas_angin)
    app_kipas_angin.start()
    
