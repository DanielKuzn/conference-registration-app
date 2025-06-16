class Conference:
    """
    Represents a conference event and manages its participants.

    Attributes:
        name (str): Name of the conference.
        location (str): Location where the conference is held.
        date (str): Date of the event (YYYY-MM-DD).
        participants (list): List of Participant objects.
    """

    def __init__(self, name: str, location: str, date: str):
        """
        Initialize a Conference instance.

        Args:
            name (str): Conference name.
            location (str): Conference location.
            date (str): Conference date.
        """
        self.name = name
        self.location = location
        self.date = date
        self.participants = []

    def add_participant(self, participant):
        """
        Add a participant to the conference.

        Args:
            participant (Participant): The participant to add.
        """
        self.participants.append(participant)

    def remove_participant(self, email: str):
        """
        Remove a participant by email.

        Args:
            email (str): Email of the participant to remove.
        """
        self.participants = [p for p in self.participants if p.email != email]

    def list_participants(self):
        """
        Return a list of participants.
        """
        for p in self.participants:
            print(p)

    def find_participant_by_email(self, email: str):
        """
        Find a participant by email.

        Args:
            email (str): Email to search for.

        Returns:
            Participant or None: Found participant or None if not found.
        """
        return next((p for p in self.participants if p.email == email), None)