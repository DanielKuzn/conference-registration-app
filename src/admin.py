class Admin:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, password: str) -> bool:
        return self._hash_password(password) == self.password_hash

    def view_statistics(self, conference):
        print(f"Total Participants: {len(conference.participants)}")
        ticket_types = {}
        for p in conference.participants:
            ticket_types[p.ticket_type] = ticket_types.get(p.ticket_type, 0) + 1
        print("Ticket Breakdown:")
        for t_type, count in ticket_types.items():
            print(f"  {t_type}: {count}")