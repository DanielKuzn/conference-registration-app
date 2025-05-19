"""
Klasa `Participant` – prosty model domenowy reprezentujący uczestnika
konferencji.

### Atrybuty
* **name** – pełne imię i nazwisko (`str`).
* **email** – adres e‑mail (`str`). Walidowany prostym – ale sensownym – regexem.
* **ticket_type** – rodzaj biletu (`str`, np. "standard", "vip").
* **registration_date** – data/godzina rejestracji (`datetime`).

### Metody
* `__str__()` – czytelna reprezentacja tekstowa.
* `to_dict()` – serializacja atrybutów do słownika.
* Walidacja e‑maila dzieje się w `__post_init__()`.
"""