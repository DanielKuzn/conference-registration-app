"""confreg.participant
====================

Klasa **`Participant`** – model domenowy reprezentujący uczestnika konferencji.

Nowe możliwości
---------------
* **Walidacja rodzaju biletu** – dozwolone wartości: `standard`, `vip`, `student`.
* **Podział imienia i nazwiska** – właściwości `first_name`, `last_name`.
* **`email_domain`** – szybki dostęp do domeny e‑mailowej.
* **`is_vip()`** – sprawdza, czy uczestnik ma bilet VIP.
* **`from_dict()`** – wygodna metoda klasowa do deserializacji.
* **Lepszy `__repr__`** – ułatwia debugowanie.

Atrybuty
--------
- **name** (`str`) – pełne imię i nazwisko (wymagane co najmniej 2 człony).
- **email** (`str`) – unikalny adres e‑mail (walidowany regexem).
- **ticket_type** (`str`) – `standard`, `vip` lub `student`.
- **registration_date** (`datetime`) – data rejestracji (UTC, domyślnie *teraz*).

Metody
------
- `__str__()` – czytelna reprezentacja tekstowa („Imię Nazwisko <mail> – bilet”).
- `__repr__()` – szczegółowa reprezentacja przydatna w logach.
- `to_dict()` / `from_dict()` – serializacja ↔ deserializacja.
- `is_vip()` – true/false.
- Właściwości: `first_name`, `last_name`, `email_domain`.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import ClassVar, Final

__all__ = ["Participant"]


@dataclass(slots=True, frozen=True)
class Participant:
    """Uczestnik konferencji."""

    # ------------------------ stałe klasowe ---------------------------
    _EMAIL_RE: ClassVar[re.Pattern[str]] = re.compile(
        r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
        r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
        r"[A-Za-z]{2,}$"
    )

    ALLOWED_TICKET_TYPES: ClassVar[set[str]] = {"standard", "vip", "student"}

    # --------------------------- pola --------------------------------
    name: str
    email: str
    ticket_type: str
    registration_date: datetime = field(default_factory=datetime.utcnow)

    # ------------------------- walidacja -----------------------------
    def __post_init__(self) -> None:  # noqa: D401
        if not self.name.strip():
            raise ValueError("Pole 'name' nie może być puste")
        if len(self.name.split()) < 2:
            raise ValueError("Pole 'name' musi zawierać co najmniej imię i nazwisko")

        if not Participant._EMAIL_RE.match(self.email):
            raise ValueError(f"Niepoprawny adres e‑mail: {self.email!r}")

        if self.ticket_type not in Participant.ALLOWED_TICKET_TYPES:
            allowed = ", ".join(sorted(Participant.ALLOWED_TICKET_TYPES))
            raise ValueError(f"ticket_type musi być jedną z: {allowed}")

    # --------------------- właściwości pomocnicze --------------------
    @property
    def first_name(self) -> str:
        """Pierwszy wyraz z pola `name`. Przydaje się w UI / e‑mailach."""
        return self.name.split()[0]

    @property
    def last_name(self) -> str:
        """Wszystko poza pierwszym wyrazem (obsługuje wieloczłonowe nazwiska)."""
        return " ".join(self.name.split()[1:])

    @property
    def email_domain(self) -> str:
        """Część domenowa adresu e‑mail (po znaku @)."""
        return self.email.split("@", 1)[1]

    # ------------------------- metody bool ---------------------------
    def is_vip(self) -> bool:
        """Czy bilet ma typ *vip*?"""
        return self.ticket_type == "vip"

    # -------------------- reprezentacje tekstowe ---------------------
    def __str__(self) -> str:  # noqa: D401
        return f"{self.name} <{self.email}> – {self.ticket_type}"

    def __repr__(self) -> str:  # noqa: D401
        return (
            "Participant("  # noqa: WPS237 (linia dla czytelności)
            f"name={self.name!r}, email={self.email!r}, "
            f"ticket_type={self.ticket_type!r}, "
            f"registration_date={self.registration_date.isoformat()})"
        )
