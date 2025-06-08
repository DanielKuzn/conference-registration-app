import unittest
import sys
import os

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from admin import Admin
from Conference import Conference
from Participant_Class_code import Participant


class TestAdmin(unittest.TestCase):
    """
    Unit tests for the Admin class.
    """

    def setUp(self):
        self.admin = Admin("admin", "securepassword")
        self.conference = Conference("PyCon", "Warsaw", "2025-08-20")
        self.participant = Participant("Alice", "alice@example.com", "Standard")
        self.conference.add_participant(self.participant)

    def test_authentication_success(self):
        self.assertTrue(self.admin.authenticate("securepassword"))

    def test_authentication_failure(self):
        self.assertFalse(self.admin.authenticate("wrongpassword"))

    def test_view_statistics(self):
        # Should run without error
        self.admin.view_statistics(self.conference)

    def test_manage_conference_method_exists(self):
        self.assertTrue(callable(self.admin.manage_conference))