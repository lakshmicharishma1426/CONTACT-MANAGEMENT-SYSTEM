import json
import os

FILE_NAME = "contacts.json"


# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("✅ Contact added successfully!")


# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


# Edit contact
def edit_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to edit: ")) - 1

        if 0 <= index < len(contacts):
            contacts[index]["name"] = input("New Name: ")
            contacts[index]["phone"] = input("New Phone: ")
            contacts[index]["email"] = input("New Email: ")

            save_contacts(contacts)
            print("✅ Contact updated successfully!")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to delete: ")) - 1

        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"✅ {deleted['name']} deleted successfully!")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            edit_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Thank you for using Contact Management System!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()