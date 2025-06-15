class PlanZajec:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def przedmioty_prowadzacego(self, prowadzacy):
        return [p for p in self.przedmioty if p.prowadzacy.lower() == prowadzacy.lower()]

    def suma_ects_dla_studenta(self, student):
        kody = set(student.kody_przedmiotow)
        suma = sum(p.ects for p in self.przedmioty if p.kod_przedmiotu in kody)
        print(f"Suma ECTS dla studenta {student.imie} {student.nazwisko}: {suma}")
        return suma
