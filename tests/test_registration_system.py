import unittest
import sys
import os
# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from RegistrationSystem_class import RegistrationSystem
from Participant_Class_code import Participant
class TestRegistrationSystem(unittest.TestCase):
    """
    Unit tests for the RegistrationSystem class.
    """
    def setUp(self):
        self.system = RegistrationSystem()
        self.system.register_participant("Ana", "ana@example.com", "Standard")
    def test_register_participant(self):
        self.assertEqual(len(self.system.participants), 1)
    def test_cancel_registration(self):
        self.system.cancel_registration("ana@example.com")
        self.assertEqual(len(self.system.participants), 0)
    def test_export_and_import_csv(self):
        filename = "test_participants.csv"
        self.system.export_to_csv(filename)
        new_system = RegistrationSystem()
        new_system.import_from_csv(filename)
        self.assertEqual(len(new_system.participants), 1)
        # Clean up
        os.remove(filename)