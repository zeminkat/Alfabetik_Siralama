liste=['elma', 'yazılım', 'merhaba', 'muzlar', 'kitap', 'çay', 'ismail', 'muz', 'dost','ılgaz']
alfabe=list(i for i in "abcçdefgğhıijklmnoöprsştuüvyz")## Alfabeyi tanımladım
def alfabetik_siralama(liste):#Fonksiyon başlangıç
    donecek_liste = list()# Yeni liste tanımladım .Bu liste üzerinde ekleme ve yer değişiklikleri yapacağım.Dönecek asıl liste bu
    kontrol = 0 # kontrol değişkeni kaç defa kontrol işlemi gerçekleştirilidiğini saymak ve ileriki durumlarda gereksiz döngüleri tespit etmek için
    for i in range(len(liste)):## ilk listenin elemanlarını almaya başlıyoruz
        if i == 0:## ikinci liste yani donecek_liste boş oluğu için aşağıdaki ilk if bloğunda 'elma'değerini atıyoruz..
            kontrol += 1
            donecek_liste.append(liste[i])
        else:#Asıl tiyatro burada başlıyor donecek_liste boş değil ve artık baştaki listedeki her değeri alıp donecek_liste'deki her değerle kontrol edeceğiz
            for z in range(len(donecek_liste)):#İlk LİSTEDEN gelen kelimeyi ikinci listedeki her değerle eşleştirmek gerekiyor..
                kontrol += 1 # döngülerin çalışma sayılarını alıyorum en sonda doğru sayıda işlem yapıp yapmadığını manuel olarak kontorl etmek için
                uzunluk = min(len(donecek_liste[z]), len(liste[i])) # kıyaslayacağım iki kelimenin uzunlukları önemli çünkü "muz" ve "muzlar" gibi bla bla
                for j in range(uzunluk):# Kısa kelimenin harf sayısı kadar kontrol etmek yeterli bunun için min fonksiyonunu yukarıda kullandım
                    if alfabe.index(donecek_liste[z][j]) < alfabe.index(liste[i][j]):## eğer yeni gelen kelime eski kelimeye göre daha sonra geliyorsa direkt ekleme yapıyorum
                        donecek_liste.append(liste[i])## ekliyoruz
                        break
                    elif alfabe.index(donecek_liste[z][j]) == alfabe.index(liste[i][j]):
                        ## BURADAKİ ELİF BLOĞUNDA kelimelerin harflerinin aynı olma durumu kontrol ediliyor
                        #Ancak kelimelerin uzunluklarının sonuna yani son harfi kontrol ettiysek ve aynıysa 
                        ##'muz' 'muzlar' gibi 2 kelime için kısa olan kelime listede diğer ögenin önüne  ekleniyor
                        print("buraya {} ile {} için {} defa bakıldı".format(donecek_liste[z], liste[i], j + 1))
                        if j == uzunluk - 1:
                            a = len(liste[i]);
                            b = len(donecek_liste[z])
                            if a == b:
                                donecek_liste.append(liste[i])
                            elif a < b:
                                gecici = donecek_liste[z]
                                donecek_liste[z] = liste[i]
                                donecek_liste.append(gecici)
                                break
                            else:
                                donecek_liste.append((liste[i]))
                                break
                    elif alfabe.index(donecek_liste[z][j]) > alfabe.index(liste[i][j]):
                        ## bu blokta yeni gelen kelimenin halihazırda liste[2]'deki kelimenin önüne ekleniyor
                        ## tampon kullandım , insert kullanmayı denedim bazı problemler oldu veyahut ben beceremedim:)
                        gecici = donecek_liste[z]
                        donecek_liste[z] = liste[i]
                        donecek_liste.append(gecici)
                        break
                    else:
                        ##Tüm ihtimalleri yukarıdaki bloklarda hallettim en azından ben öyle varsayıyorum
                        ## Buraya ekleme çıkarmalar yaptığım için tutuyorum:)
                        pass
                    
    ##Asıl sorun burada başlıyor
    ##Normalde en baştaki 10 tane kelimemizi sıralamak istediğimizde aklımdaki algoritmaya göre
    ##Elma kelimesi boş olan dönecek_listesine eklenecek
    ## Ardından gelen yazılım kelimesi sadece elma ile kontrol edilecek
    ## 'MERHABA' 2 KERE
    ## 'MUZLAR' 3 KERE>>
    ## .....    .....
    ## ILGAZ 9 KERE
    ## SONUÇ >> (9*8)/2 = 36 KERE KONTROL ETSE Kİ KAĞIT ÜZERİNDE YAPSAK BU KADAR KONTROL YETERLİ OLUYOR
    ## ANCAK ÇALIŞTIRDIĞINIZDA GÖRECEKSİNİZ 512 TUR DÖNÜYOR ve Bazı DEĞERLERİ bir kaç kez yazıyor
    ##512 KERE DEĞER YAZDIRDIĞI İÇİN AYNI KELİMENİN TEKRARI DURUMLAR OLUYORDU BUNU AŞAĞIDAKİ BLOKLA ÇÖZDÜM
    ## ANCAK BU İŞLEVSEL DEĞİL BENİ FONKSİYONU YAZDIĞIM BÖLÜMDE GEREKSİZ TEKRAR EDEN YERLER VAR VE TESPİT EDEMEDİM
    for i in donecek_liste:
        if donecek_liste.count(i) > 1:
            for j in range(donecek_liste.count(i) - 1):
                donecek_liste.remove(i)
    return donecek_liste


print(alfabetik_siralama(liste))
