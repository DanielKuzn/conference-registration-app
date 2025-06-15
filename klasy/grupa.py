import csv

class Grupa:
    def __init__(self):
        self.studenci = []

    def dodaj_studenta(self, student):
        self.studenci.append(student)

    def studenci_z_numerem_indeksu(self, numer):
        return [s for s in self.studenci if s.numer_indeksu == numer]

    def srednia_ocen_grupy(self):
        wszystkie_oceny = [ocena for s in self.studenci for ocena in s.oceny]
        if wszystkie_oceny:
            return sum(wszystkie_oceny) / len(wszystkie_oceny)
        return 0.0

    def eksportuj_do_csv(self, nazwa_pliku):
        with open(nazwa_pliku, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['imie', 'nazwisko', 'numer_indeksu'])
            for s in self.studenci:
                writer.writerow([s.imie, s.nazwisko, s.numer_indeksu])
        print(f"Dane wyeksportowane do pliku {nazwa_pliku}")

    def studenci_ze_srednia_wyzsza_niz(self, prog):
        return [s for s in self.studenci if s.srednia_ocen() > prog]

