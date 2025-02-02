def stworz_album(nazwa_artysty, tytul_albumu, liczba_utworow=0):
    
    if liczba_utworow == 0:
        liczba_utworow = "None"

    stworz_album_slownik = {"nazwa_artysty":nazwa_artysty,"tytul_albumu":tytul_albumu, "liczba_utworow":liczba_utworow}     
    return stworz_album_slownik

albom_funkcja = stworz_album ("Swen", "Kuzia", 5)
albom_funkcja = stworz_album ("Alks", "Kukurydza")

print(albom_funkcja)

def stworz_album(nazwa_artysty, tytul_albumu, liczba_utworow=None):
    """Tworzy słownik opisujący album muzyczny."""
    album = {
        "nazwa_artysty": nazwa_artysty,
        "tytul_albumu": tytul_albumu,
    }
    if liczba_utworow:  # Dodanie liczby utworów tylko jeśli została podana
        album["liczba_utworow"] = liczba_utworow
    return album

# Tworzenie trzech różnych albumów
album1 = stworz_album("Artysta 1", "Album Pierwszy")
album2 = stworz_album("Artysta 2", "Album Drugi", liczba_utworow=10)
album3 = stworz_album("Artysta 3", "Album Trzeci")

# Wydrukowanie wyników
print(album1)
print(album2)
print(album3)

# Wywołanie funkcji z liczbą utworów
album_z_utworami = stworz_album("Artysta 4", "Album Czwarty", liczba_utworow=15)
print(album_z_utworami)