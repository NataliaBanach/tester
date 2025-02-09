# Moduł konwerter.py

PRZELICZNIK = 0,61 # 1 km = 0,61 mil

def km_na_mile(km):
    """Konwertuje kilometry na mile."""
    return km * PRZELICZNIK

def mile_na_km(mile):
    """Konwertuje mile na kilometry."""
    return mile / PRZELICZNIK