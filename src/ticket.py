# New class for ticket
class Ticket:
    """
    Represents a ticket type with a price and access level.
    """

    def __init__(self, ticket_type: str, price: float, access_level: str):
        self.ticket_type = ticket_type
        self.price = price
        self.access_level = access_level

    def get_price(self) -> float:
        return self.price

    def __str__(self):
        return f"{self.ticket_type} - ${self.price} ({self.access_level})"