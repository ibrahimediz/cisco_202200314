#Access Modifiers  public private
"""
__gizli => gizli değişken
__gizli_ => gizli değişken
__gizli__ => GİZLİ DEĞİL
""" 

# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli= "Jamiryo"
    
# obj1 = A(1)
# print(obj1.yetki)
# print(obj1.__gizli) # AttributeError: 'A' object has no attribute '__gizli'

###################################### getter and setter and property##########################
################ 1 ##################
# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli= "Jamiryo"
    
#     def gizliGetir(self):
#         if self.yetki == 1:
#             return self.__gizli
#         else:
#             raise Exception("Yetki Hatası")
    
# obj1 = A(1)
# obj2 = A(2)
# print(obj1.gizliGetir())
# print(obj2.gizliGetir())
############### 2 ########################
class A:
    def __init__(self,yetki):
        self.yetki = yetki
        self.__gizli= "Jamiryo"

    @property
    def gizli(self):  # getter
        if self.yetki == 1:
            return self.__gizli
        else:
            raise Exception("Yetki Hatası")
    
obj1 = A(1)
obj2 = A(2)
print(obj1.gizli)
# print(obj2.gizli)
#################### 3 ########################
class A:
    def __init__(self,yetki):
        self.yetki = yetki
        self.__gizli= 2

    @property
    def gizli(self):  # getter
        if self.yetki == 1:
            return self.__gizli
        else:
            raise Exception("Yetki Hatası")

    @gizli.setter
    def gizli(self,param):
        if self.yetki == 1:
            if isinstance(param, int) and param in range(1,10):
                self.__gizli = param
            else:
                raise Exception("Değer Hatası")
        else:
            raise Exception("Yetki Hatası")

    @gizli.deleter
    def gizli(self):
        if self.yetki == 1:
            self.__gizli *= -1
        else:
            raise Exception("Yetki Hatası")


obj1 = A(1)
obj2 = A(2)
print(obj1.gizli)
obj1.gizli = 5
print(obj1.gizli)
del obj1.gizli
print(obj1.gizli)
# print(obj2.gizli)