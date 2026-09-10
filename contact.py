contacts = []


def add_contact():
    print("\n--- Add Contact ---")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("\nContact added successfully!")


def view_contacts():
    print("\n--- Contact List ---")

    if len(contacts) == 0:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print("\nContact", i)
        print("Name    :", contact["name"])
        print("Phone   :", contact["phone"])
        print("Email   :", contact["email"])
        print("Address :", contact["address"])


def search_contact():
    print("\n--- Search Contact ---")

    search = input("Enter name or phone number: ").lower()

    found = False

    for contact in contacts:
        if (search in contact["name"].lower() or
                search in contact["phone"]):

            print("\nContact Found!")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    print("\n--- Update Contact ---")

    name = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            print("\nLeave blank if you don't want to change a detail.")

            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            print("\nContact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")

    name = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("\nContact deleted successfully!")
            return

    print("Contact not found.")


# Main Program
while True:

    print("\n==============================")
    print("       CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\nInvalid choice! Please try again.")