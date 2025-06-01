from datetime import datetime

class Participant:
    """
    Represents a conference participant.
    """

    def __init__(self, name: str, email: str, ticket_type: str):
        self.name = name
        self.email = email
        self.ticket_type = ticket_type
        self.registration_date = datetime.now()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "ticket_type": self.ticket_type,
            "registration_date": self.registration_date.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.ticket_type}"