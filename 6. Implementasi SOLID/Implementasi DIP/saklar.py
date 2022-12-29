from barang_elektronik import BarangElektronik

class Saklar:
    
    def __init__(self, item: BarangElektronik, keaktifan: bool = False):
        self.__item = item
        self.__keaktifan = keaktifan
    
    def berubah(self):
        if self.__keaktifan:
            self.__item.berhenti()
            self.__keaktifan = False
        else:
            self.__item.beroperasi()
            self.__keaktifan = True





