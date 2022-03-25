from abc import ABC,abstractmethod,abstractclassmethod


class A(ABC):
    @abstractmethod
    def vur(self):
        pass 

class B(A):
    def vur(self):
        pass

# objA = A()
objB = B()