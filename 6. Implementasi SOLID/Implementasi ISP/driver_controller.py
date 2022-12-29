from interface.driver_operation import DriverOperation

class DriverController(DriverOperation):
    
    def menolak_pesanan(self) -> None:
        print("Driver menolak pengantaran karena lokasi tidak terjangkau")
        
    def mengantarkan_pesanan(self) -> None:
        print("Driver mengantarkan pemesanan dari penjual ke pembeli")


