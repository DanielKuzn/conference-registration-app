import csv
from Participant_Class_code import Participant


class RegistrationSystem:
    """
    Handles the logic for registering participants and managing data.
    """

    def __init__(self):
        self.participants = []

    def register_participant(self, name: str, email: str, ticket_type: str):
        participant = Participant(name, email, ticket_type)
        self.participants.append(participant)
        return participant

    def cancel_registration(self, email: str):
        self.participants = [p for p in self.participants if p.email != email]

    def export_to_csv(self, filename: str):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email", "ticket_type", "registration_date"])
            writer.writeheader()
            for p in self.participants:
                writer.writerow(p.to_dict())

    def import_from_csv(self, filename: str):
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                participant = Participant(row["name"], row["email"], row["ticket_type"])
                self.participants.append(participant)
