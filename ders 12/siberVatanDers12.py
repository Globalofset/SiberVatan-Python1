"""
def saatlik_calisan(toplam_calısma_saati):
    saatlik_ucret = 50
    if toplam_calısma_saati <=40:
        maas = toplam_calısma_saati * saatlik_ucret
    else:
        normal_calisma_saati = 40
        fazla_mesai_saati = toplam_calısma_saati -40
        maas = normal_calisma_saati *saatlik_ucret + (fazla_mesai_saati*1.5) * saatlik_ucret/2
    return maas

def hesaplakomisyon(aylik_satis):
    sabit_maas = 500
    komisyon_oranı = 0.05
    komisyon = aylik_satis * komisyon_oranı
    maas = sabit_maas + komisyon
    return maas

while True:
    odeme_kodu = int(input(" ödeme kodu girin 1 saatlik 2 komisyonlu"))
    if odeme_kodu == 1:
        calisma_saati = int(input("çalışma saatinizi giriniz"))
        maas = saatlik_calisan(calisma_saati)
        print("maaşınız",maas)
        break
    elif odeme_kodu==2:
        satis=float(input("Ayınca kaç tl elde edildi? "))
        maas = hesaplakomisyon(satis)
        print("komisyonlu  maaşınız",maas)
        break
else:
    raise ValueError()

"""
sicaklik_degerleri = [5,-15,12,2,30,18,-5,35,-18,8]
def sicaklik_sayisi(sicakliklar):
    
    sicaklik =  { 
        "(-20) - (0)":0,
        "(0) - (+20) ":0,
        "(+20) - (+40)":0
    }
    for deger in sicakliklar:
        if -20 <= sicaklik < 0:
            sicaklik_degerleri["(-20)-(0)"]+=1
        elif 0 <= sicaklik <20:
            sicaklik_degerleri["(0)-(20)"]+=1
        elif 20 <= sicaklik <40:
            sicaklik_degerleri["(20)-(40)"]+=1
        
    for aralik,sayi  in sicaklik_degerleri.items():
        print(aralik)
        print(f"Bu aralıktaki sayı : {len(sicakliklar)}")
            
print(sicaklik_sayisi(sicaklik_degerleri))











