#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <limits>
using namespace std;

// ---------------------- Contact Class ----------------------
class Contact {
private:
    int contactID;
    string firstName, lastName, category;
    vector<string> phoneNumbers;
    vector<string> emails;

public:
    Contact() {}
    Contact(int id, string f, string l, string c) {
        contactID = id;
        firstName = f;
        lastName = l;
        category = c;
    }

    int getID() { return contactID; }
    string getLastName() { return lastName; }

    void addPhone(string p) { phoneNumbers.push_back(p); }
    void addEmail(string e) { emails.push_back(e); }

    void editDetails() {
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Enter new first name: ";
        getline(cin, firstName);
        cout << "Enter new last name: ";
        getline(cin, lastName);
        cout << "Enter new category: ";
        getline(cin, category);

        phoneNumbers.clear();
        emails.clear();

        int n;
        cout << "How many phone numbers? ";
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        for (int i = 0; i < n; i++) {
            string p;
            cout << "Enter phone number " << i + 1 << ": ";
            getline(cin, p);
            phoneNumbers.push_back(p);
        }

        cout << "How many emails? ";
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        for (int i = 0; i < n; i++) {
            string e;
            cout << "Enter email " << i + 1 << ": ";
            getline(cin, e);
            emails.push_back(e);
        }
    }

    void display() {
        cout << "ID: " << contactID << "\n";
        cout << "Name: " << firstName << " " << lastName << "\n";
        cout << "Category: " << category << "\n";
        cout << "Phone Numbers:\n";
        for (string p : phoneNumbers) cout << " - " << p << "\n";
        cout << "Emails:\n";
        for (string e : emails) cout << " - " << e << "\n";
        cout << "----------------------------\n";
    }

    string toFileString() {
        ostringstream oss;
        oss << contactID << "," << firstName << "," << lastName << "," << category;
        for (string p : phoneNumbers) oss << ",P:" << p;
        for (string e : emails) oss << ",E:" << e;
        return oss.str();
    }

    void fromFileString(string line) {
        stringstream ss(line);
        string part;
        vector<string> tokens;
        while (getline(ss, part, ',')) tokens.push_back(part);

        contactID = stoi(tokens[0]);
        firstName = tokens[1];
        lastName = tokens[2];
        category = tokens[3];

        phoneNumbers.clear();
        emails.clear();
        for (int i = 4; i < tokens.size(); i++) {
            if (tokens[i].rfind("P:", 0) == 0)
                phoneNumbers.push_back(tokens[i].substr(2));
            else if (tokens[i].rfind("E:", 0) == 0)
                emails.push_back(tokens[i].substr(2));
        }
    }
};

// ---------------------- Global Data ----------------------
vector<Contact> contacts;
int nextID = 1;

// ---------------------- Functions ----------------------
void loadContacts() {
    ifstream fin("contacts.dat");
    if (!fin) return;

    string line;
    while (getline(fin, line)) {
        Contact c;
        c.fromFileString(line);
        contacts.push_back(c);
        if (c.getID() >= nextID) nextID = c.getID() + 1;
    }
    fin.close();
}

void saveContacts() {
    ofstream fout("contacts.dat");
    for (Contact &c : contacts) {
        fout << c.toFileString() << endl;
    }
    fout.close();
}

void addContact() {
    string f, l, c;
    cout << "Enter first name: ";
    getline(cin, f);
    cout << "Enter last name: ";
    getline(cin, l);
    cout << "Enter category: ";
    getline(cin, c);

    Contact con(nextID++, f, l, c);

    int n;
    cout << "How many phone numbers? ";
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    for (int i = 0; i < n; i++) {
        string p;
        cout << "Enter phone " << i + 1 << ": ";
        getline(cin, p);
        con.addPhone(p);
    }

    cout << "How many emails? ";
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    for (int i = 0; i < n; i++) {
        string e;
        cout << "Enter email " << i + 1 << ": ";
        getline(cin, e);
        con.addEmail(e);
    }

    contacts.push_back(con);
    cout << "Contact added successfully!\n";
}


void searchContact() {
    int choice;
    cout << "Search by 1. ID  2. Last Name: ";
    if (!(cin >> choice)) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Invalid input!\n";
        return;
    }
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if (choice == 1) {
        int id;
        cout << "Enter Contact ID: ";
        cin >> id;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        for (Contact &c : contacts)
            if (c.getID() == id) {
                c.display();
                return;
            }
        cout << "Contact not found.\n";
    } else if (choice == 2) {
        string lname;
        cout << "Enter Last Name: ";
        getline(cin, lname);
        bool found = false;
        for (Contact &c : contacts) {
            if (c.getLastName() == lname) {
                c.display();
                found = true;
            }
        }
        if (!found) cout << "Contact not found.\n";
    } else {
        cout << "Invalid choice!\n";
    }
}

void deleteContact() {
    int id;
    cout << "Enter Contact ID to delete: ";
    if (!(cin >> id)) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Invalid input!\n";
        return;
    }
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (auto it = contacts.begin(); it != contacts.end(); ++it) {
        if (it->getID() == id) {
            contacts.erase(it);
            cout << "Contact deleted.\n";
            return;
        }
    }
    cout << "Contact not found.\n";
}

void updateContact() {
    int id;
    cout << "Enter Contact ID to update: ";
    if (!(cin >> id)) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Invalid input!\n";
        return;
    }
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (Contact &c : contacts)
        if (c.getID() == id) {
            c.editDetails();
            cout << "Contact updated.\n";
            return;
        }
    cout << "Contact not found.\n";
}

void displayAllContacts() {
    cout << "\nAll Contacts:\n";
    for (Contact &c : contacts)
        c.display();
}

// ---------------------- Main Function ----------------------
int main() {
    loadContacts();
    int choice;

    do {
        cout << "\n==== Contact Management System ====\n";
        cout << "1. Add New Contact\n";
        cout << "2. Search for a Contact\n";
        cout << "3. Delete a Contact\n";
        cout << "4. Update a Contact\n";
        cout << "5. Display All Contacts\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";

        if (!(cin >> choice)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input! Please enter a number between 1 and 6.\n";
            continue;
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        switch (choice) {
        case 1: addContact(); break;
        case 2: searchContact(); break;
        case 3: deleteContact(); break;
        case 4: updateContact(); break;
        case 5: displayAllContacts(); break;
        case 6:
            saveContacts();
            cout << "All data saved. Goodbye!\n";
            break;
        default:
            cout << "Invalid choice! Please select a number between 1 and 6.\n";
        }
    } while (choice != 6);

    return 0;
}
