import random # importujemy modul do losowania liczb

# losowanie liczby z zakresu od 1 do 10

losowa = random.randint(1, 10)
print("Wylosowana liczba to:", losowa)

# wylosujemy 5 liczb z zakresu od 1 do 10, zapiszmy je do listy

lista_losowych = random.sample(range(1, 11), 5)
print("Wylosowane liczby to:", lista_losowych)

liczba_1 = int(input("Podaj pierwszą liczbę 1: "))
liczba_2 = int(input("Podaj drugą liczbę 2: "))

losowa = random.randint(liczba_1, liczba_2)
print("Wylosowana liczba to:", losowa)