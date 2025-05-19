"""
Klasa `Participant` – prosty model domenowy reprezentujący uczestnika
konferencji.

### Atrybutyy
* **name** – pełne imię i nazwisko (`str`).
* **email** – adres e‑mail (`str`). Walidowany prostym – ale sensownym – regexem.
* **ticket_type** – rodzaj biletu (`str`, np. "standard", "vip").
* **registration_date** – data/godzina rejestracji (`datetime`).

### Metody
* `__str__()` – czytelna reprezentacja tekstowa.
* `to_dict()` – serializacja atrybutów do słownika.
* Walidacja e‑maila dzieje się w `__post_init__()`.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import ClassVar

__all__ = ["Participant"]


@dataclass(slots=True, frozen=True)
class Participant:
    """Uczestnik konferencji."""

    # wzorzec do walidacji adresu e‑mail.
    _EMAIL_RE: ClassVar[re.Pattern[str]] = re.compile(
        r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
        r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
        r"[A-Za-z]{2,}$"
    )

    name: str
    email: str
    ticket_type: str
    registration_date: datetime = field(default_factory=datetime.utcnow)

    # ------------------------------------------------------------------
    # Walidacja pól
    # ------------------------------------------------------------------
    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Pole 'name' nie może być puste")
        if not Participant._EMAIL_RE.match(self.email):
            raise ValueError(f"Niepoprawny adres e‑mail: {self.email!r}")
        if not self.ticket_type.strip():
            raise ValueError("Pole 'ticket_type' nie może być puste")

    # ------------------------------------------------------------------
    # Metody użytkowe
    # ------------------------------------------------------------------
    def __str__(self) -> str:
        """Przyjazna reprezentacja: „Imię Nazwisko <mail> – bilet”."""
        return f"{self.name} <{self.email}> – {self.ticket_type}"

    def to_dict(self) -> dict[str, str | datetime]:
        """Zwraca atrybuty obiektu jako słownik (przydatne np. do JSON)."""
        return asdict(self)
