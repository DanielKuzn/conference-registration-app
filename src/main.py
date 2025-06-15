from admin import Admin
from Conference import Conference
from RegistrationSystem_class import RegistrationSystem
from Participant_Class_code import Participant

def main():
    """
    Main entry point of the Conference Registration System CLI.
    """
    print("Welcome to the Conference Registration System\n")

    # Setup default admin and conference (could be extended to load from config or DB)
    admin = Admin("admin", "admin123")
    conference = Conference("Python Conference", "Krakow", "2025-09-10")
    system = RegistrationSystem()

    while True:
        print("\nMain Menu:")
        print("1. Register a Participant")
        print("2. Cancel Registration")
        print("3. Export Participants to CSV")
        print("4. Import Participants from CSV")
        print("5. Admin Login")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            ticket_type = input("Ticket Type: ")
            participant = system.register_participant(name, email, ticket_type)
            conference.add_participant(participant)
            print("Participant registered successfully.")

        elif choice == "2":
            email = input("Enter the email to cancel registration: ")
            system.cancel_registration(email)
            conference.remove_participant(email)
            print("Registration cancelled if found.")

        elif choice == "3":
            filename = input("Enter filename to export (e.g., participants.csv): ")
            system.export_to_csv(filename)
            print(f"Participants exported to {filename}")

        elif choice == "4":
            filename = input("Enter filename to import from (e.g., participants.csv): ")
            system.import_from_csv(filename)
            for p in system.participants:
                if not conference.find_participant_by_email(p.email):
                    conference.add_participant(p)
            print(f"Participants imported from {filename}")

        elif choice == "5":
            username = input("Admin Username: ")
            password = input("Admin Password: ")
            if username == admin.username and admin.authenticate(password):
                print("Admin login successful.")
                admin.manage_conference(conference)
            else:
                print("Invalid admin credentials.")

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
