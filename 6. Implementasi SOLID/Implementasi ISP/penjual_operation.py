from interface.penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod

class PenjualOperation(PenolakanOperation, ABC):
    
    @abstractmethod
    def menolak_pesanan(self) -> None:
        # isi method ini boleh diganti dengan "pass" saja
        super().menolak_pesanan()
        
    @abstractmethod
    def menyiapkan_pesanan(self) -> None:
        pass



