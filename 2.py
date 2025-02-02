def koszulka(valueA, valueB): 
    print(f"Rozmiar koszulki: {valueA} , Tekst na koszulce: {valueB}")



koszulka("s", "Harri Poter")
# koszulka( rozmiar="m", wiadomosc="Piter Pen")
x = "z"
y = "Popa Pen"
 
koszulka('zopa', y)
koszulka(x, y)
#koszulka(y)

koszulka(valueA=x, valueB=y)
koszulka(valueB=y, valueA=x)


