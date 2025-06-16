import unittest
import sys
import os
import tempfile

# Add src/ directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from RegistrationSystem_class import RegistrationSystem
from Conference import Conference
from Participant_Class_code import Participant

class TestConferenceSystemIntegration(unittest.TestCase):
    """
    Integration tests that verify multiple components work together.
    """

    def test_register_and_add_participant_to_conference(self):
        system = RegistrationSystem()
        conference = Conference("Dev Summit", "Gdansk", "2025-11-20")
        participant = system.register_participant("Anna", "anna@example.com", "Standard")
        conference.add_participant(participant)
        self.assertEqual(len(system.participants), 1)
        self.assertEqual(len(conference.participants), 1)
        self.assertEqual(conference.participants[0].email, "anna@example.com")

    def test_admin_view_statistics(self):
        from admin import Admin
        admin = Admin("admin", "pass123")
        conference = Conference("AI Expo", "Poznan", "2025-12-01")
        conference.add_participant(Participant("Bob", "bob@example.com", "Standard"))
        conference.add_participant(Participant("Carol", "carol@example.com", "VIP"))
        try:
            admin.view_statistics(conference)
        except Exception as e:
            self.fail(f"admin.view_statistics raised an exception: {e}")

    def test_export_and_import_participants(self):
        # Arrange
        system = RegistrationSystem()
        conference = Conference("ML Conf", "Lodz", "2025-09-15")
        participant = system.register_participant("Eva", "eva@example.com", "Standard")
        conference.add_participant(participant)
     # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_file:
            filename = temp_file.name
     # Act
        system.export_to_csv(filename)
        new_system = RegistrationSystem()
        new_system.import_from_csv(filename)
     # Clean up
        os.remove(filename)
     # Assert
        self.assertEqual(len(new_system.participants), 1)
        self.assertEqual(new_system.participants[0].email, "eva@example.com")

if __name__ == '__main__':
    unittest.main()