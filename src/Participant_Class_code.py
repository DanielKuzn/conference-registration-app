from datetime import datetime

class Participant:
    """
    Represents a participant of a conference.

    Attributes:
        name (str): The participant's full name.
        email (str): The participant's email address.
        ticket_type (str): Type of ticket the participant holds.
    """

    def __init__(self, name: str, email: str, ticket_type: str):
        """
        Initialize a Participant instance.

        Args:
            name (str): Participant's name.
            email (str): Participant's email.
            ticket_type (str): Type of ticket.
        """
        self.name = name
        self.email = email
        self.ticket_type = ticket_type
        self.registration_date = datetime.now()

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the Participant.
        """
        return {
            "name": self.name,
            "email": self.email,
            "ticket_type": self.ticket_type,
            "registration_date": self.registration_date.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.ticket_type}"