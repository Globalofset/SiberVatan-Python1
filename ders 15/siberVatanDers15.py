# class Person():
#     def _init_(self,fname,lname):
#         self.fname= fname
#         self.lname= lname
#         print("person olustu")
#     def ben_kimim(self):
#         print("ben kişiyim")
        
        
# class Teacher(Person):
#     def _init_(self, fname, lname,branch):
#         super()._init_(fname, lname)
#         self.branch=branch
#         print("teacher olustu ")
#     def ben_kimim(self):
#         print("ben ort")


# class Student(Person):
#     def _init_(self,fname,lname,number):
#         self.number=number
#         Person._init_(self,lname,fname)
#         print("student olustu")
#     def ben_kimim(self):
#         print("ben ogrenci")

# p1 = Person (fname="lebron" , lname="james")
# print(p1.lname)
# t1 = Teacher(fname="esra", lname="orhan", branch="edebiyat")
# print(t1)
# s1 = Student(fname="apo", lname="akyel", number=335)
# print(s1)

# p1.ben_kimim()
# s1.ben_kimim()
# t1.ben_kimim()   #overrading

class Superclass():
    def _init_(self,sayi1,sayi2):
        self.sayi1= sayi1
        self.sayi2= sayi2
    def hesaplama(self):
        pass
class Toplama(Superclass):
    def _init_(self, sayi1, sayi2):
        super()._init_(sayi1, sayi2)
    def hesaplama(self):
        return self.sayi1+self.sayi2
class Cıkartma(Superclass):
    def _init_(self, sayi1, sayi2):
        super()._init_(sayi1, sayi2)
    def hesaplama(self):
        return self.sayi1-self.sayi2   
class Bolme(Superclass):
    def _init_(self, sayi1, sayi2):
        super()._init_(sayi1, sayi2)
    def hesaplama(self):
        return self.sayi1/self.sayi2
class çarpma(Superclass):
    def _init_(self, sayi1, sayi2):
        super()._init_(sayi1, sayi2)
    def hesaplama(self):
        return self.sayi1*self.sayi2
        

t1= Toplama(sayi1=50 , sayi2=5).hesaplama()
print(t1)
c1= Cıkartma(sayi1=50, sayi2=5).hesaplama()
print(c1)
b1= Bolme(sayi1=50,sayi2=5).hesaplama()
print(b1)
ç1= çarpma(sayi1=50, sayi2=5).hesaplama
print(ç1)