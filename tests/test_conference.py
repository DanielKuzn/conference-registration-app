import unittest
import sys
import os

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Conference import Conference
from Participant_Class_code import Participant

class TestConference(unittest.TestCase):
    """
    Unit tests for the Conference class.
    """

    def setUp(self):
        self.conference = Conference("AI Summit", "Berlin", "2025-09-15")
        self.participant = Participant("Tom", "tom@example.com", "Standard")
        self.conference.add_participant(self.participant)

    def test_add_participant(self):
        self.assertEqual(len(self.conference.participants), 1)

    def test_remove_participant(self):
        self.conference.remove_participant("tom@example.com")
        self.assertEqual(len(self.conference.participants), 0)

    def test_find_participant_by_email(self):
        result = self.conference.find_participant_by_email("tom@example.com")
        self.assertIsNotNone(result)
        self.assertEqual(result.email, "tom@example.com")