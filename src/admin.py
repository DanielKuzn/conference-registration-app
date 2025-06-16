from hashlib import sha256
from Conference import Conference

class Admin:
    """
    Represents an administrator with privileges to manage a conference.

    Attributes:
        username (str): The admin's username.
        password (str): The admin's password.
    """

    def __init__(self, username: str, password: str):
        """
        Initialize an Admin instance.

        Args:
            username (str): Admin username.
            password (str): Admin password.
        """
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        """
        Returns a SHA-256 hash of the provided password.
        """
        return sha256(password.encode()).hexdigest()

    def authenticate(self, password: str) -> bool:
        """
        Authenticate the admin using the password.

        Args:
            password (str): Password to check.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        return self._hash_password(password) == self.password_hash

    def view_statistics(self, conference: Conference):
        """
        Display the number of registered participants.

        Args:
            conference (Conference): The conference to inspect.
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
        Perform basic administrative actions on the conference.

        Args:
            conference (Conference): The conference to manage.
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