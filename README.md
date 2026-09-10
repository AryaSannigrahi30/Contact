# 📱 Contact Book

A simple and beginner-friendly Contact Book application built using Python. This project allows users to store and manage contact information including name, phone number, email, and address. Users can add, view, search, update, and delete contacts through a simple command-line interface.

## 📌 Features

- Add new contacts.
- Store name, phone number, email, and address.
- View all saved contacts.
- Search contacts by name or phone number.
- Update existing contact details.
- Delete contacts.
- Handles contacts using Python lists and dictionaries.
- Simple and easy-to-use command-line interface.
- Beginner-friendly Python project.

## 🛠️ Technologies Used

- Python
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements

## 📂 Project Structure

Contact-Book/
│
├── contact_book.py
└── README.md

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository using the following command:

```bash
git clone https://github.com/your-username/Contact-Book.git
```

Open the project folder:

```bash
cd Contact-Book
```

Run the Python program:

```bash
python contact_book.py
```

The Contact Book menu will appear on the screen. Select an option by entering the corresponding number.

## 💻 Example Output

```text
==============================
       CONTACT BOOK
==============================
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
==============================
Enter your choice: 1

--- Add Contact ---
Enter name: Rahul
Enter phone number: 9876543210
Enter email: rahul@gmail.com
Enter address: Kolkata

Contact added successfully!
```

### View Contacts

```text
==============================
       CONTACT BOOK
==============================
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
==============================
Enter your choice: 2

--- Contact List ---

Contact 1
Name    : Rahul
Phone   : 9876543210
Email   : rahul@gmail.com
Address : Kolkata
```

### Search Contact

```text
--- Search Contact ---
Enter name or phone number: Rahul

Contact Found!
Name    : Rahul
Phone   : 9876543210
Email   : rahul@gmail.com
Address : Kolkata
```

### Update Contact

```text
--- Update Contact ---
Enter the name of the contact to update: Rahul

Leave blank if you don't want to change a detail.
Enter new name: Rahul Das
Enter new phone number:
Enter new email: rahuldas@gmail.com
Enter new address:

Contact updated successfully!
```

### Delete Contact

```text
--- Delete Contact ---
Enter the name of the contact to delete: Rahul Das

Contact deleted successfully!
```

## 🧠 How It Works

The program starts with an empty list called `contacts` which is used to store all contact information.

Each contact is stored as a Python dictionary containing four details:

```python
contact = {
    "name": name,
    "phone": phone,
    "email": email,
    "address": address
}
```

The program uses separate functions for different operations:

### 1. Add Contact

The `add_contact()` function asks the user to enter the name, phone number, email, and address. These details are stored in a dictionary and added to the `contacts` list.

### 2. View Contacts

The `view_contacts()` function displays all saved contacts. If there are no contacts, it displays a message saying that no contacts were found.

### 3. Search Contact

The `search_contact()` function allows the user to search for a contact using their name or phone number.

### 4. Update Contact

The `update_contact()` function searches for a contact by name and allows the user to change any of its details. Leaving a field blank keeps the existing information unchanged.

### 5. Delete Contact

The `delete_contact()` function searches for a contact by name and removes it from the contact list.

### 6. Main Menu

The main program uses a `while` loop to continuously display the Contact Book menu. The user can select different operations until they choose the Exit option.

## 📋 Available Options

| Option | Function | Description |
|--------|----------|-------------|
| 1 | Add Contact | Adds a new contact |
| 2 | View Contacts | Displays all saved contacts |
| 3 | Search Contact | Searches by name or phone number |
| 4 | Update Contact | Updates existing contact details |
| 5 | Delete Contact | Deletes a contact |
| 6 | Exit | Closes the program |

## 🎯 Purpose

The purpose of this project is to create a simple Contact Book application while practicing basic Python programming concepts such as lists, dictionaries, functions, loops, conditional statements, user input, and data manipulation.

## 📚 Learning Outcome

Through this project, I learned how to use Python lists and dictionaries to store and manage data. I also learned how to create and use functions, take user input, use loops and conditional statements, search and modify data, and build a simple menu-driven command-line application.

This project helped me gain practical experience in developing a basic data management application using Python.

## 🔍 Programming Concepts Used

- Variables
- Lists
- Dictionaries
- Functions
- User Input
- `if`, `elif`, and `else` statements
- `while` loop
- `for` loop
- `return` statement
- `break` and `continue`
- String methods
- Data searching
- Data updating
- Data deletion
- Menu-driven programming

## ⚠️ Current Limitation

The current version stores contacts only while the program is running. When the program is closed, all contacts are removed because the data is stored temporarily in memory.

## 🚀 Future Improvements

The project can be improved in the future by:

- Saving contacts permanently using a file.
- Using JSON or CSV for data storage.
- Using an SQLite database.
- Adding contact categories or groups.
- Adding better phone number and email validation.
- Adding a graphical user interface (GUI).
- Adding a password or login system.
- Adding sorting options for contacts.
- Adding backup and restore functionality.

## 🙏 Acknowledgement

This project was created as part of a Python Internship Task at Pinnacle Labs. It helped me understand and practice fundamental Python programming concepts through a practical Contact Book application.

## 👨‍💻 Author

**Arya Sannigrahi**

CSE Student
