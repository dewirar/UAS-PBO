from interface.penjual_operation import PenjualOperation

class PenjualController(PenjualOperation):
    
    def menolak_pesanan(self) -> None:
        print("Penjual menolak pesanan karena stok telah habis")
        
    def menyiapkan_pesanan(self) -> None:
        print("Penjual menyiapkan pesanan baru sesuai pilihan pembeli")


