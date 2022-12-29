from controller.driver_controller import DriverController
from controller.pembeli_controller import PembeliController
from controller.penjual_controller import PenjualController

pembeli = PembeliController()
penjual_1 = PenjualController()
penjual_2 = PenjualController()
driver_1 = DriverController()
driver_2 = DriverController()

pembeli.memesan_pesanan()
penjual_1.menolak_pesanan()
penjual_2.menyiapkan_pesanan()
driver_1.menolak_pesanan()
driver_2.mengantarkan_pesanan()




