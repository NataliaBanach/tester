import random

for _ in range(5):  
    liczba = random.randint(1, 100)  
    print(liczba)


import random

wynik = []  # Tworzymy pustą listę na wylosowane liczby

for i in range(5):  # Pętla wykonująca się 5 razy
    liczba = random.randint(1, 100)  # zapisanie wartosci losowej do zmiennej
    wynik.append(wynik)  # dodanie wylosowanej liczby do listy

print("Wylosowane liczby to:", wynik)  # Wydrukowanie listy z wylosowanymi liczbami    
 
import random

liczby = []  # Tworzymy pustą listę na wylosowane liczby

for _ in range(5):  
    liczby.append(random.randint(1, 100))  # Losujemy liczbę i dodajemy do listy

print("Wylosowane liczby to:", liczby)  # Wyświetlamy wynik