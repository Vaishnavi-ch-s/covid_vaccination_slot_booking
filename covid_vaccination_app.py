import datetime

# --- Data Classes ---
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class Slot:
    def __init__(self, date, capacity):
        self.date = date
        self.capacity = capacity
        self.booked_users = []

    def book(self, user):
        if len(self.booked_users) < self.capacity:
            self.booked_users.append(user)
            return True
        return False

class Certificate:
    def __init__(self, user, date):
        self.user = user
        self.date = date

    def generate(self):
        return f"--- Vaccination Certificate ---\nName: {self.user.username}\nDate: {self.date}\nStatus: Vaccinated ✅"

# --- Sample Data ---
slots = [
    Slot("2025-07-25", 2),
    Slot("2025-07-26", 2),
]

users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "pass123", "role": "user"},
    "user2": {"password": "pass456", "role": "user"}
}

# --- Functions ---
def login():
    username = input("Username: ")
    password = input("Password: ")
    user_data = users_db.get(username)

    if user_data and user_data["password"] == password:
        return User(username, user_data["role"])
    print("❌ Invalid credentials")
    return None

def admin_panel():
    print("\n🔐 Admin Panel - Available Slots:")
    for i, slot in enumerate(slots):
        print(f"{i+1}. Date: {slot.date} | Capacity: {slot.capacity} | Booked: {len(slot.booked_users)}")

def user_panel(user):
    print("\n📅 Available Slots:")
    for i, slot in enumerate(slots):
        print(f"{i+1}. {slot.date} - {slot.capacity - len(slot.booked_users)} spots left")

    choice = int(input("Enter slot number to book: ")) - 1

    if 0 <= choice < len(slots):
        slot = slots[choice]
        if slot.book(user):
            cert = Certificate(user, slot.date)
            print("\n✅ Booking successful!")
            print(cert.generate())
        else:
            print("❌ Slot full! Choose another.")
    else:
        print("❌ Invalid slot selection.")

# --- Main Program ---
def main():
    print("🛡️ Covid-19 Vaccination Slot Booking System")
    user = login()
    if not user:
        return

    if user.role == "admin":
        admin_panel()
    else:
        user_panel(user)

if __name__ == "__main__":
    main()