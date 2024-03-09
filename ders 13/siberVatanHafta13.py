# """
# def sayikontrol(sayi):
#     basamaklar =set(str(sayi))
#     if basamaklar == 1:
#         return 1
#     else:
#         return 2
    
# a = [233,777,99999999,81,36,90,88,11,61]
# for sayi in a:
#     if sayikontrol(sayi):
#         print(f"{sayi} basamaklar birbirine eşit")
#     else:
#         print(f"{sayi} basamaklar birbirine eşit değil")



# """

# liste = [10,20,30]

# print(type(liste))
# """
# class Person:
#     adress = "bilgi yok"
#     def __init__(self,name,lastname,dyıl):
#         self.name = name
#         self.lastname =lastname
#         self.dyıl = dyıl
# p1 = Person(name="berat",lastname="ozcan",dyıl="2007")
# print(p1)
# print(type(p1))
# print("benim adım",p1.name,"soy adım",p1.name,"adres",p1.adress)
# """
# class person1:
#     def __init__(self,ad,soyad,adres,year):
#         self.ad = ad
#         self.soyad=soyad
#         self.adres=adres
#         self.year=year
#     def intro(self):
#         print("merhaab ben "+self.ad)
#        # print("yaşım", 2024-self.year)

#     def yas_hesabi(self):
#         return 2024 - self.year
# p2= person1(ad="mehmet",soyad="sayan",adres="5k",year=int(2007))
# print(p2)
# print(type(p2))
# print("benim adım",p2.ad,"soyadım",p2.soyad,"adresim",p2.adres,"dogum yılı",p2.year)
# p2.intro()


# class Daire:
#     pi = 3.14
#     def __init__(self,r):
#         self.r = r

#     def cevre(self):
#         return 2 * self.pi * self.r
    
#     def alan(self):
#         return self.pi * (self.r ** 2)

# d = Daire(5)
# print("çevre", d.cevre())
# print("alan", d.alan())


class square:
    def __init__  (self ,kenar):
        self.kenar = kenar
    def alan(self):
        return self.kenar*self.kenar
    def cevre(self,cevre):
        return 2*(self.cevre+self.cevre)
        self.kenar = kenar
kare=quare1 = square(6)
print(kare.alan())

















































