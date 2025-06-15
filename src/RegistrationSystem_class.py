import csv
from Participant_Class_code import Participant


class RegistrationSystem:
    """
    Manages the registration and data persistence of participants.

    Attributes:
        participants (list): List of registered participants.
    """

    def __init__(self):
        """
        Initializes the registration system with an empty list of participants.
        """
        self.participants = []

    def register_participant(self, name: str, email: str, ticket_type: str):
        """
        Registers a new participant.

        Args:
            name (str): Name of the participant.
            email (str): Email of the participant.
            ticket_type (str): Ticket type selected.

        Returns:
            Participant: The registered participant object.
        """
        participant = Participant(name, email, ticket_type)
        self.participants.append(participant)
        return participant

    def cancel_registration(self, email: str):
        """
        Cancels a registration by email.

        Args:
            email (str): The email of the participant to cancel.
        """
        self.participants = [p for p in self.participants if p.email != email]

    def export_to_csv(self, filename: str):
        """
        Exports participant data to a CSV file.

        Args:
            filename (str): Path to the output CSV file.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email", "ticket_type", "registration_date"])
            writer.writeheader()
            for p in self.participants:
                writer.writerow(p.to_dict())

    def import_from_csv(self, filename: str):
        """
        Imports participant data from a CSV file.

        Args:
            filename (str): Path to the input CSV file.
        """
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                participant = Participant(row["name"], row["email"], row["ticket_type"])
                self.participants.append(participant)
