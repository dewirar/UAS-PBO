from persegi import Persegi
from persegi_controller import PersegiController


class PersegiView:
    
    def show_luas(self, persegi: Persegi, persegi_controller: PersegiController):
        print (persegi_controller.hitung_luas(persegi))
        
    def show_keliling(self, persegi: Persegi, persegi_controller: PersegiController):
        print (persegi_controller.hitung_keliling(persegi))
        
        
        
        
        