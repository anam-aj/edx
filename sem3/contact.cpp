// contact_manager.cpp
// Compile: g++ -std=c++17 contact_manager.cpp -o contact_manager

#include <bits/stdc++.h>
using namespace std;

struct LabeledValue {
    string label;
    string value;
};

class Contact {
private:
    int contactID;
    string firstName;
    string lastName;
    string category;
    vector<LabeledValue> phones; // label -> number
    vector<LabeledValue> emails; // label -> address

public:
    Contact() : contactID(0) {}
    Contact(int id, string fn, string ln, string cat)
        : contactID(id), firstName(move(fn)), lastName(move(ln)), category(move(cat)) {}

    int getID() const { return contactID; }
    string getLastName() const { return lastName; }
    string getFullName() const { return firstName + " " + lastName; }

    void setFirstName(const string &s) { firstName = s; }
    void setLastName(const string &s)  { lastName = s; }
    void setCategory(const string &s)  { category = s; }

    void addPhone(const string &label, const string &number) {
        phones.push_back({label, number});
    }
    void addEmail(const string &label, const string &addr) {
        emails.push_back({label, addr});
    }

    bool removePhoneByIndex(size_t idx) {
        if (idx < phones.size()) { phones.erase(phones.begin() + idx); return true; }
        return false;
    }
    bool removeEmailByIndex(size_t idx) {
        if (idx < emails.size()) { emails.erase(emails.begin() + idx); return true; }
        return false;
    }

    void displayFull() const {
        cout << "ID: " << contactID << "\n";
        cout << "Name: " << firstName << " " << lastName << "\n";
        cout << "Category: " << category << "\n";
        cout << "Phones:\n";
        if (phones.empty()) cout << "  (none)\n";
        for (size_t i = 0; i < phones.size(); ++i)
            cout << "  [" << i << "] " << phones[i].label << ": " << phones[i].value << "\n";
        cout << "Emails:\n";
        if (emails.empty()) cout << "  (none)\n";
        for (size_t i = 0; i < emails.size(); ++i)
            cout << "  [" << i << "] " << emails[i].label << ": " << emails[i].value << "\n";
    }

    void displaySummary() const {
        cout << setw(6) << contactID << " | " << left << setw(25) << (firstName + " " + lastName)
             << " | " << category << "\n";
    }

    // Serialization
    string serialize() const {
        // Multi-line block format, easy to parse.
        ostringstream oss;
        oss << "BEGIN_CONTACT\n";
        oss << "ID:" << contactID << "\n";
        oss << "FirstName:" << firstName << "\n";
        oss << "LastName:" << lastName << "\n";
        oss << "Category:" << category << "\n";
        oss << "PhonesCount:" << phones.size() << "\n";
        for (const auto &p : phones) {
            // label and value separated by '|'
            oss << "Phone:" << p.label << "|" << p.value << "\n";
        }
        oss << "EmailsCount:" << emails.size() << "\n";
        for (const auto &e : emails) {
            oss << "Email:" << e.label << "|" << e.value << "\n";
        }
        oss << "END_CONTACT\n";
        return oss.str();
    }

    static bool startsWith(const string &s, const string &pref) {
        return s.size() >= pref.size() && s.substr(0, pref.size()) == pref;
    }

    // Parse one contact from an input stream; returns true on success
    static bool deserializeFrom(istream &is, Contact &out) {
        string line;
        // Seek to BEGIN_CONTACT
        while (getline(is, line)) {
            if (line == "BEGIN_CONTACT") break;
        }
        if (is.eof() && line != "BEGIN_CONTACT") return false;

        int id = 0;
        string fn, ln, cat;
        vector<LabeledValue> phones;
        vector<LabeledValue> emails;

        while (getline(is, line)) {
            if (line == "END_CONTACT") break;
            if (startsWith(line, "ID:")) {
                id = stoi(line.substr(3));
            } else if (startsWith(line, "FirstName:")) {
                fn = line.substr(10);
            } else if (startsWith(line, "LastName:")) {
                ln = line.substr(9);
            } else if (startsWith(line, "Category:")) {
                cat = line.substr(9);
            } else if (startsWith(line, "PhonesCount:")) {
                // ignore; handled by reading Phone: lines
            } else if (startsWith(line, "Phone:")) {
                string payload = line.substr(6);
                auto pos = payload.find('|');
                if (pos != string::npos) {
                    string label = payload.substr(0, pos);
                    string val = payload.substr(pos + 1);
                    phones.push_back({label, val});
                }
            } else if (startsWith(line, "EmailsCount:")) {
                // ignore
            } else if (startsWith(line, "Email:")) {
                string payload = line.substr(6);
                auto pos = payload.find('|');
                if (pos != string::npos) {
                    string label = payload.substr(0, pos);
                    string val = payload.substr(pos + 1);
                    emails.push_back({label, val});
                }
            }
        }

        if (fn.empty() && ln.empty() && id == 0 && cat.empty() && phones.empty() && emails.empty()) {
            return false; // likely nothing read
        }

        out = Contact(id, fn, ln, cat);
        out.phones = move(phones);
        out.emails = move(emails);
        return true;
    }
};

static string readLineTrimmed(const string &prompt) {
    cout << prompt;
    string s;
    getline(cin, s);
    // trim both ends
    auto l = s.find_first_not_of(" \t\r\n");
    if (l == string::npos) return "";
    auto r = s.find_last_not_of(" \t\r\n");
    return s.substr(l, r - l + 1);
}

static int readInt(const string &prompt, int minVal = INT_MIN, int maxVal = INT_MAX) {
    while (true) {
        cout << prompt;
        string line;
        if (!getline(cin, line)) return minVal;
        try {
            int x = stoi(line);
            if (x < minVal || x > maxVal) {
                cout << "Please enter a number between " << minVal << " and " << maxVal << ".\n";
                continue;
            }
            return x;
        } catch (...) {
            cout << "Invalid integer. Try again.\n";
        }
    }
}

void loadContacts(const string &filename, vector<Contact> &contacts) {
    ifstream ifs(filename);
    if (!ifs) {
        // file not found — start empty
        return;
    }
    while (true) {
        Contact c;
        if (Contact::deserializeFrom(ifs, c)) {
            contacts.push_back(move(c));
        } else break;
    }
}

void saveContacts(const string &filename, const vector<Contact> &contacts) {
    ofstream ofs(filename, ios::trunc);
    if (!ofs) {
        cerr << "Error: cannot open " << filename << " for writing.\n";
        return;
    }
    for (const auto &c : contacts) {
        ofs << c.serialize();
    }
}

// utility: find index by ID
int findIndexByID(const vector<Contact> &v, int id) {
    for (size_t i = 0; i < v.size(); ++i) if (v[i].getID() == id) return (int)i;
    return -1;
}

int nextAvailableID(const vector<Contact> &v) {
    int mx = 0;
    for (const auto &c : v) mx = max(mx, c.getID());
    return mx + 1;
}

// case-insensitive compare helper
bool iequals(const string &a, const string &b) {
    if (a.size() != b.size()) return false;
    for (size_t i = 0; i < a.size(); ++i)
        if (tolower((unsigned char)a[i]) != tolower((unsigned char)b[i])) return false;
    return true;
}

int main() {
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    const string datafile = "contacts.dat";
    vector<Contact> contacts;
    loadContacts(datafile, contacts);
    cout << "Contact Management System (file: " << datafile << ")\n";

    while (true) {
        cout << "\nMenu:\n";
        cout << "1. Add New Contact\n2. Search for a Contact\n3. Delete a Contact\n4. Update a Contact\n5. Display All Contacts\n6. Exit\n";
        int choice = readInt("Choose an option (1-6): ", 1, 6);
        if (choice == 1) {
            int id = nextAvailableID(contacts);
            string fn = readLineTrimmed("First name: ");
            string ln = readLineTrimmed("Last name: ");
            string cat = readLineTrimmed("Category: ");
            Contact c(id, fn, ln, cat);

            // Phones
            while (true) {
                string add = readLineTrimmed("Add phone? (y/n): ");
                if (add.empty() || tolower(add[0]) != 'y') break;
                string lbl = readLineTrimmed("  Phone label (e.g., Mobile, Home): ");
                string num = readLineTrimmed("  Number: ");
                c.addPhone(lbl, num);
            }
            // Emails
            while (true) {
                string add = readLineTrimmed("Add email? (y/n): ");
                if (add.empty() || tolower(add[0]) != 'y') break;
                string lbl = readLineTrimmed("  Email label (e.g., Personal, Work): ");
                string addr = readLineTrimmed("  Address: ");
                c.addEmail(lbl, addr);
            }

            contacts.push_back(move(c));
            cout << "Contact added with ID " << id << ".\n";

        } else if (choice == 2) {
            cout << "Search by: 1) ID  2) Last Name\n";
            int s = readInt("Choose (1-2): ", 1, 2);
            if (s == 1) {
                int id = readInt("Enter Contact ID: ");
                int idx = findIndexByID(contacts, id);
                if (idx >= 0) contacts[idx].displayFull();
                else cout << "Contact not found.\n";
            } else {
                string ln = readLineTrimmed("Enter last name (case-insensitive exact match): ");
                bool found = false;
                for (const auto &c : contacts) {
                    if (iequals(c.getLastName(), ln)) {
                        c.displayFull();
                        cout << "------------------------\n";
                        found = true;
                    }
                }
                if (!found) cout << "No contact with last name '" << ln << "' found.\n";
            }

        } else if (choice == 3) {
            int id = readInt("Enter Contact ID to delete: ");
            int idx = findIndexByID(contacts, id);
            if (idx < 0) {
                cout << "Contact not found.\n";
            } else {
                cout << "Are you sure you want to delete contact " << contacts[idx].getFullName() << " (ID " << id << ")? (y/n): ";
                string ans; getline(cin, ans);
                if (!ans.empty() && tolower(ans[0]) == 'y') {
                    contacts.erase(contacts.begin() + idx);
                    cout << "Deleted.\n";
                } else {
                    cout << "Cancelled.\n";
                }
            }

        } else if (choice == 4) {
            int id = readInt("Enter Contact ID to update: ");
            int idx = findIndexByID(contacts, id);
            if (idx < 0) {
                cout << "Contact not found.\n";
            } else {
                Contact &c = contacts[idx];
                cout << "Editing contact:\n";
                c.displayFull();
                cout << "Update options:\n";
                cout << "1. First name\n2. Last name\n3. Category\n4. Add phone\n5. Remove phone\n6. Add email\n7. Remove email\n8. Done\n";
                while (true) {
                    int u = readInt("Choose option: ", 1, 8);
                    if (u == 1) {
                        string s = readLineTrimmed("New first name: ");
                        if (!s.empty()) c.setFirstName(s);
                    } else if (u == 2) {
                        string s = readLineTrimmed("New last name: ");
                        if (!s.empty()) c.setLastName(s);
                    } else if (u == 3) {
                        string s = readLineTrimmed("New category: ");
                        if (!s.empty()) c.setCategory(s);
                    } else if (u == 4) {
                        string lbl = readLineTrimmed("Phone label: ");
                        string num = readLineTrimmed("Number: ");
                        c.addPhone(lbl, num);
                    } else if (u == 5) {
                        cout << "Phones:\n";
                        c.displayFull();
                        int pi = readInt("Index of phone to remove: ");
                        if (c.removePhoneByIndex((size_t)pi)) cout << "Removed.\n";
                        else cout << "Invalid index.\n";
                    } else if (u == 6) {
                        string lbl = readLineTrimmed("Email label: ");
                        string addr = readLineTrimmed("Address: ");
                        c.addEmail(lbl, addr);
                    } else if (u == 7) {
                        cout << "Emails:\n";
                        c.displayFull();
                        int ei = readInt("Index of email to remove: ");
                        if (c.removeEmailByIndex((size_t)ei)) cout << "Removed.\n";
                        else cout << "Invalid index.\n";
                    } else if (u == 8) {
                        cout << "Finished updating.\n";
                        break;
                    }
                }
            }

        } else if (choice == 5) {
            cout << setw(6) << "ID" << " | " << left << setw(25) << "Full Name" << " | " << "Category\n";
            cout << string(60, '-') << "\n";
            for (const auto &c : contacts) c.displaySummary();

        } else if (choice == 6) {
            saveContacts(datafile, contacts);
            cout << "Contacts saved. Exiting.\n";
            break;
        }
    }

    return 0;
}
