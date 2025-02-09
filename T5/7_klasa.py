class Samochod:
    # definicja klasy
    def __init__(self, marka, model):
        # self reprezentuje nowo tworzona instancje/obiekt klasy
        self.marka = marka # ustawiamy atrybuty "marka" obiektu
        self.model = model # ustawiamy atrybuty "model" obiektu
        self.predkosc = 0 # ustawiamy predkosc poczatkowa na 0

    def uruchom_silnik(self):
        print("Silnik uruchomiony")
        self.wlaczony_silnik = True   

    def przyspiesz(self, wartosc):
        # zakladamy ze atrybut ptedkosc istnieje
        self.predkosc += wartosc

moj_samochod = Samochod("Toyota", "Corolla") # tworzymy obiekt klasy Samochod