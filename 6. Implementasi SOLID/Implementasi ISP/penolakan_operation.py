from abc import ABC, abstractmethod

class PenolakanOperation(ABC):
    
    @abstractmethod
    def menolak_pesanan(self) -> None:
        pass
    



