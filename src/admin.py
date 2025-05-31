from hashlib import sha256
from conference import Conference

class Admin:
    """
    Represents an admin user who can manage the conference system.
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        """
        Returns a SHA-256 hash of the provided password.
        """
        return sha256(password.encode()).hexdigest()

    def authenticate(self, password: str) -> bool:
        """
        Checks if the provided password matches the stored hash.
        """
        return self._hash_password(password) == self.password_hash

    def view_statistics(self, conference: Conference):
        """
        Prints statistics about participants in a conference.
        """
        print(f"Conference: {conference.name}")
        print(f"Location: {conference.location}")
        print(f"Date: {conference.date}")
        print(f"Total Participants: {len(conference.participants)}")
        ticket_counts = {}
        for p in conference.participants:
            ticket_counts[p.ticket_type] = ticket_counts.get(p.ticket_type, 0) + 1
        print("Ticket Breakdown:")
        for ticket_type, count in ticket_counts.items():
            print(f"  {ticket_type}: {count}")

    def manage_conference(self, conference: Conference):
        """
        Provides an interactive interface to manage a given conference.
        """
        while True:
            print("\nConference Management Menu:")
            print("1. View Participants")
            print("2. Remove Participant")
            print("3. View Statistics")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                conference.list_participants()
            elif choice == '2':
                email = input("Enter email of participant to remove: ")
                conference.remove_participant(email)
                print("Participant removed if found.")
            elif choice == '3':
                self.view_statistics(conference)
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")