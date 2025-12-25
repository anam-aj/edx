#include <iostream>
#include <iomanip>
#include <string>


using namespace std;


int main() {

    // Component 4: Custom component - Program information
    cout << "\n------------- COMPONENT 4: PROGRAM INFO ------------" << endl;

    // Get current date/time info (simulated)
    string currentDate = "2023-08-15";
    string userName = "C++ Learner";
    int linesOfCode = 75;

    // Format and display program information
    cout << "Program: Multi-Component Example" << endl;
    cout << "Author: " << userName << endl;
    cout << "Date: " << currentDate << endl;
    cout << "Code Statistics:" << endl;
    cout << " - Lines of code: " << linesOfCode << endl;
    cout << " - Header files: 3" << endl;
    cout << " - Components: 4" << endl;

    // Display a progress bar (simulated)
    cout << "Completion: [";
    int progress = 80; // 80% complete
    // A loop allows something to happen over and over again
    for (int i = 0; i < 20; i++) {
        if (i < progress/5) cout << "=";
        else cout << " ";
    }
    cout << "] " << progress << "%" << endl;
    
    return 0;
}
