class Przedmiot:
    def __init__(self, nazwa, kod_przedmiotu, prowadzacy, ects):
        self.nazwa = nazwa
        self.kod_przedmiotu = kod_przedmiotu
        self.prowadzacy = prowadzacy
        self.ects = ects

    def opis(self):
        return f"Przedmiot: {self.nazwa}, Kod: {self.kod_przedmiotu}, Prowadzący: {self.prowadzacy}, ECTS: {self.ects}"
