from abc import ABC, abstractmethod


class BarangElektronik(ABC):
    
    @abstractmethod
    def beroperasi(self):
        pass
    
    @abstractmethod
    def berhenti(self):
        pass




