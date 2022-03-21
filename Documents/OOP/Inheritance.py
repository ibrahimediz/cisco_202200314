################### Inheritance #############################
# class A:
#     def __init__(self,a=1):
#         self.a = a

#     def soyle(self):
#         print("A Sınıfından Çalıştım")
    
#     def soyleA(self):
#         print(self.a)


# class B(A): # A sınıfından miras aldı
#     def __init__(self,a,b):# yukarıdaki constructor üzerine yazdım override
#         super().__init__(a) # buradaki super() ifadesi miras alınan sınıfı temsil eder
#         self.b = b


# obj1 = B(1,2)
# obj1.soyleA()
# obj1.soyle()
################### Multiple Inheritance #############################
class A:
    def __init__(self,a):
        self.a = a

    def soyle(self):
        print("A Sınıfından Çalıştım")
    
    def soyleA(self):
        print(self.a)

class B:
    def __init__(self,b):
        self.b = b

    def soyle(self):
        print("B sınıfından Çalıştım")
    
    def soyleB(self):
        print(self.b)


class C(A,B):
    def __init__(self,a,b,c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c
    
    def soyleC(self):
        print(self.c)

obj1 = C(1,2,3)
obj1.soyleA()
obj1.soyleB()
obj1.soyleC()
obj1.soyle()
