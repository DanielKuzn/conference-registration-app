from przedmiot import Przedmiot
from student import Student
from grupa import Grupa
from plan_zajęć import PlanZajec

# Tworzenie przedmiotów i planu
p1 = Przedmiot("Matematyka", "MATH101", "Dr Kowalski", 5)
p2 = Przedmiot("Programowanie", "CS102", "Dr Nowak", 6)

plan = PlanZajec()
plan.dodaj_przedmiot(p1)
plan.dodaj_przedmiot(p2)

# Tworzenie studentów
s1 = Student("Anna", "Kowalska", "12345")
s1.oceny = [4.5, 5.0]
s1.kody_przedmiotow = ["MATH101", "CS102"]

s2 = Student("Jan", "Nowak", "67890")
s2.oceny = [3.0, 3.5]
s2.kody_przedmiotow = ["MATH101"]

# Grupa studentów
grupa = Grupa()
grupa.dodaj_studenta(s1)
grupa.dodaj_studenta(s2)

# Testy funkcjonalności
print(p1.opis())
print("Średnia ocen grupy:", grupa.srednia_ocen_grupy())
print("Studenci z indeksem 12345:", [s.imie for s in grupa.studenci_z_numerem_indeksu("12345")])
print("Studenci ze średnią > 4.0:", [s.imie for s in grupa.studenci_ze_srednia_wyzsza_niz(4.0)])
grupa.eksportuj_do_csv("studenci.csv")
print("Przedmioty dr Nowak:", [p.nazwa for p in plan.przedmioty_prowadzacego("dr nowak")])
plan.suma_ects_dla_studenta(s1)
