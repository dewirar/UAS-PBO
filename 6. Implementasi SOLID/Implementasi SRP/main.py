from persegi import Persegi
from persegi_controller import PersegiController
from persegi_view import PersegiView

persegi = Persegi(6)
penghitung_persegi = PersegiController()
penampil_persegi = PersegiView()

penampil_persegi.show_luas(persegi, penghitung_persegi)
penampil_persegi.show_keliling(persegi, penghitung_persegi)




