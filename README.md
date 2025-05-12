# Conference Registration System

A Python-based project to manage participant registration for a conference. The system allows users to register, view participants, manage ticket types, and administer the entire registration process.

## 🔧 Project Requirements

- Python 3.8+
- Basic knowledge of object-oriented programming
- Git for version control

## 🚀 Features

- Register and manage participants
- Assign ticket types (Standard, VIP, etc.)
- Export and import participants via CSV
- Admin authentication and statistics
- Clean object-oriented design with 5+ classes:
  - `Participant`: Stores user info
  - `Conference`: Holds event data and participant list
  - `Ticket`: Ticket types with pricing and access
  - `RegistrationSystem`: Main logic for registration and data handling
  - `Admin`: Handles admin-level access and operations

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/conference-registration.git
cd conference-registration
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

## 📦 Example Usage

```python
from src.registration_system import RegistrationSystem

system = RegistrationSystem()
system.register_participant(
    name="Alice Johnson",
    email="alice@example.com",
    ticket_type="VIP"
)

system.export_to_csv("data/participants.csv")
```

You can run the main program:

```bash
python src/main.py
```

## 🧪 Running Tests

```bash
pytest tests/
```

---

Developed by a student team as part of a software engineering project.
