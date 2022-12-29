from saklar import Saklar
from kipas_angin import KipasAngin
from lampu import Lampu

lampu = Lampu()
kipas = KipasAngin()

saklar_1 = Saklar(lampu)
saklar_1.berubah()
saklar_1.berubah()
saklar_1.berubah()
print("--------------")
saklar_2 = Saklar(kipas)
saklar_2.berubah()
saklar_2.berubah()
saklar_2.berubah()


