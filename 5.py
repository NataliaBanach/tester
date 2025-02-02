def miasta_panstwa(miasto, ludnosc=0, panstwo="Polska"):

    #sprawdzenie czy ludnosc jest zero
    if ludnosc==0:
        #jesli zero-NaN
        ludnosc = "NaN"
        #jesli nie jest zero - to jest ok


    miasto_panstwo_slownik = {"panstwo": panstwo, "miasto":miasto, "ludnosc":ludnosc}
    return miasto_panstwo_slownik


miasto_funkcja = miasta_panstwa("Berlin", 0, "Niemcy")

print(miasto_funkcja)
