import os 


os.path.dirname("c:/Users/ber78/software/sibarvatan/ders 16")
os.listdir()
#print(os.getcwd()) #gecikmeyi durduruyoruz

try:
    file=open("isimler.txt","r") #read modu ile açılıyor
    print(file.read()) #tüm dosyanın iceriklerini yazdırıyor
except FileNotFoundError :
    print("Dosya bulunamadı.")
finally:
    if file is not None:
        file.close() #eğer dosya açılmışsa     
        with open ("isimler.txt", "w") as f: 
            