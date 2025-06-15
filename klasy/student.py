class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []  # lista ocen z różnych przedmiotów
        self.kody_przedmiotow = []  # kody przedmiotów, na które uczęszcza

    def srednia_ocen(self):
        if self.oceny:
            return sum(self.oceny) / len(self.oceny)
        return 0.0
