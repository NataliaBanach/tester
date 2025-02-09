# Importujemy nasz moduł konwerter

import konwerter

kilometry = 6
mile = 3

wynik_1 = konwerter.km_na_mile(kilometry)
wynik_2 = konwerter.mile_na_km(mile)

print(f"{kilometry} km to {wynik_1:.2f} mil")
print(f"{mile} mil to {wynik_2:.2f} km")