import unittest
 import sys
 import os
 # Add the src directory to sys.path
 sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
 from ticket import Ticket
 class TestTicket(unittest.TestCase):
    """
    Unit tests for the Ticket class.
    """
    def test_ticket_attributes(self):
        ticket = Ticket("VIP", 150.0, "Full Access")
        self.assertEqual(ticket.ticket_type, "VIP")
        self.assertEqual(ticket.price, 150.0)
        self.assertEqual(ticket.access_level, "Full Access")
    def test_get_price(self):
        ticket = Ticket("Standard", 50.0, "Basic Access")
        self.assertEqual(ticket.get_price(), 50.0)
    def test_str_representation(self):
        ticket = Ticket("VIP", 200.0, "All Access")
        self.assertIn("VIP", str(ticket))
        self.assertIn("200.0", str(ticket))