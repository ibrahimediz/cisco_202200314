from abc import ABC,abstractmethod



class Hero(ABC):
    @abstractmethod
    def vur(self):
        pass 

    @abstractmethod
    def darbe(self):
        pass


    @abstractmethod
    def durum(self):
        pass