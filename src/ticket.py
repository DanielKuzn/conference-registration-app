class Ticket:
    """
    Represents a conference ticket.

    Attributes:
        ticket_type (str): Type of the ticket (e.g., 'Standard', 'VIP').
        price (float): Price of the ticket.
    """

    def __init__(self, ticket_type: str, price: float, access_level: str):
        """
        Initializes a Ticket instance.

        Args:
            ticket_type (str): Type of the ticket.
            price (float): Price of the ticket.
        """
        self.ticket_type = ticket_type
        self.price = price
        self.access_level = access_level

    def get_price(self) -> float:
        """
        Return the price of the ticket.
        """
        return self.price

    def __str__(self):
        return f"{self.ticket_type} - ${self.price} ({self.access_level})"