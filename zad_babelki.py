pensje = [4200, 5100, 4800, 4500, 4700, 5300, 4900, 35000, 4400]

def babelki():
    for j in range(8):
        
        for i in range(len(pensje) - 1):
            if pensje[i] > pensje[i + 1]:
                temp = pensje[i]
                pensje[i] = pensje[i + 1]
                pensje[i + 1] = temp
        print(j+1, pensje)

babelki()

print("Najmniejsza pensja: ", pensje[0])
print("Największa pensja: ", pensje[8])

srednia = int(sum(pensje) / len(pensje))
print("Średnia wynosi: ", srednia)

mediana = pensje[len(pensje) // 2]
print("Mediana: ", mediana)

liczba_mniej = 0

for s in range(8):
    if s < srednia:
        liczba_mniej+=1

print("Liczba pracowników zarabiajacych mniej niz średnia: ", liczba_mniej)

srednia_bezprezesa = int(sum(pensje[:-1]) / len(pensje[:-1]))
print("Średnia prezesa wynosi: ", srednia_bezprezesa)

print(f"Reklama firmy jest niepoprawna, ponieważ średnia płacy pracowników wynosi {srednia}. Mediana wynosząca {mediana} mówi nam to samo, tylko w zaokrąglonym wyniku.")

# dodatkowe

nowy_pracownik = 6000

pensje.append(nowy_pracownik)

babelki()

mediana = pensje[len(pensje) // 2]
print("Mediana: ", mediana)
