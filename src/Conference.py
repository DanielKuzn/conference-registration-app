class Conference:
    """
    Represents a conference event and holds registered participants.
    """

    def __init__(self, name: str, location: str, date: str):
        self.name = name
        self.location = location
        self.date = date
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, email: str):
        self.participants = [p for p in self.participants if p.email != email]

    def list_participants(self):
        for p in self.participants:
            print(p)

    def find_participant_by_email(self, email: str):
        return next((p for p in self.participants if p.email == email), None)