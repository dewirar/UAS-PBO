from abc import ABC, abstractmethod

class ProductDelivery(ABC):
    
    def __init__(self, price: int, name: str):
        self.__price = price
        self.__name = name
    
    def get_price(self) -> int:
        return self.__price
    
    def get_name(self) -> str:
        return self.__name
        
    @abstractmethod
    def calculate_delivery(self) -> int:
        pass
    
    
    
