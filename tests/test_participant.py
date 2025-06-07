import unittest
import sys
import os

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Participant_Class_code import Participant

class TestParticipant(unittest.TestCase):
    """
    Unit tests for the Participant class.
    """

    def test_to_dict(self):
        p = Participant("John", "john@example.com", "VIP")
        data = p.to_dict()
        self.assertEqual(data["name"], "John")
        self.assertEqual(data["email"], "john@example.com")
        self.assertEqual(data["ticket_type"], "VIP")

    def test_str_representation(self):
        p = Participant("Jane", "jane@example.com", "Standard")
        self.assertIn("Jane", str(p))
        self.assertIn("jane@example.com", str(p))
