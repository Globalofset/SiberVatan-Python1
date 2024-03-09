#open("yenidosya.txt","w")

# "w" write -> yazma modu,yoks oluşturur içeriği silip ekleme yapar 
# "a" append -> ekleme modu,yoks oluşturmaz var ise ekler ,yoksa içeriğini getirir ve ekler 
#"x"  exclusive -> sadece bir tane yoksa açılabilir ,var ise hata verir 
#"r"  read -> okuma modu ,yoks oluşturmaz ,içeriği alır 
"""
file = open("yenidosya.txt",'w')
print(file)
file.close()

file_dizin = open("C:/Users/ber78/software/sibarvatan/yenidosya.txt","w",encoding='utf-8')
file_dizin.write("GLOBALOFSET")
file.close()
file = open("yenidosya.txt","a",encoding='utf-8')
file.write("Berat Ozcan")
file.close()

try:
    filee = open("yenidosya.txt",'x')
    filee.close()
except FileExistsError:
    print("Dosya zaten var")

"""





























