liste=['elma', 'yazılım', 'merhaba', 'muzlar', 'kitap', 'çay', 'ismail', 'muz', 'dost','ılgaz']
alfabe=list(i for i in "abcçdefgğhıijklmnoöprsştuüvyz")## Alfabeyi tanımladım
def alfabetik_siralama(liste):#Fonksiyon başlangıç
    donecek_liste = list()
    kontrol = 0
    for i in range(len(liste))
        if i == 0:
            kontrol += 1
            donecek_liste.append(liste[i])
        else:
            for z in range(len(donecek_liste)):
                kontrol += 1 
                uzunluk = min(len(donecek_liste[z]), len(liste[i])) 
                for j in range(uzunluk):
                    if alfabe.index(donecek_liste[z][j]) < alfabe.index(liste[i][j]):
                        donecek_liste.append(liste[i])
                        break
                    elif alfabe.index(donecek_liste[z][j]) == alfabe.index(liste[i][j]):
                       
                     
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
                       
                        gecici = donecek_liste[z]
                        donecek_liste[z] = liste[i]
                        donecek_liste.append(gecici)
                        break
                    else:
      
                        pass
                    
    for i in donecek_liste:
        if donecek_liste.count(i) > 1:
            for j in range(donecek_liste.count(i) - 1):
                donecek_liste.remove(i)
    return donecek_liste


print(alfabetik_siralama(liste))
