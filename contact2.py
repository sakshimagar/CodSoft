
def add_contact(contacts):
    print("\nEnter contact information:")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email ID: ")
    address = input("Address: ")

    new_contact = {'name': name, 'phone number': phone , 'email ID': email, 'address': address}
    contacts.append(new_contact)

    print("Contact added successfully in contact list!!")

def view_contacts(contacts):
    print("\nContact List:")
    if not contacts:
        print("Contact not found.")
    else:
        for contact in contacts:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-" * 20)

def search_contact(contacts):
    query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]

    print("\nSearch contact:")
    if not results:
        print("No matching contacts found.")
    else:
        for result in results:
            print(f"\nName: {result['name']}")
            print(f"Phone: {result['phone']}")
            print(f"Email: {result['email']}")
            print(f"Address: {result['address']}")
            print("-" * 20)

def update_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("\nEnter the number of the contact to update: ")) - 1
        contact = contacts[index]
        print(f"\nUpdating contact: {contact['name']}")
        contact['name'] = input("New Name: ")
        contact['phone'] = input("New Phone Number: ")
        contact['email'] = input("New Email: ")
        contact['address'] = input("New Address: ")
        print("Contact updated successfully!")
    except (ValueError, IndexError):
        print("Invalid input. Update failed.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("\nEnter the number of the contact to delete: ")) - 1
        deleted_contact = contacts.pop(index)
        print(f"Deleted contact: {deleted_contact['name']}")
    except (ValueError, IndexError):
        print("Invalid input. Deletion failed.")

def contact_book():
    contacts = []

    while True:
        print("\nCONTACT BOOK\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Quitting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    contact_book()
c
