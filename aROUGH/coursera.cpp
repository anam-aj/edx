#include <iostream>
#include <string>

using namespace std;

double performOperation(double a, char op, double b);

int main() {
    // Display welcome message
    cout << "=======================================" << endl;
    cout << "    MATHEMATICAL EXPRESSION EVALUATOR  " << endl;
    cout << "=======================================" << endl;
    cout << "This program evaluates mathematical expressions" << endl;
    cout << "using various operators and precedence rules." << endl << endl;
    // Main program code will go here
    bool continueCalculations = true;
    while (continueCalculations) {
        double num1, num2;
        char op, choice;
        cout << "\nEnter a simple expression (number operator number): ";
        cin >> num1 >> op >> num2;
        double result = performOperation(num1, op, num2);
        cout << "Result: " << num1 << " " << op << " " << num2 << " = " << result << endl;
        cout << "\nContinue with another calculation? (y/n): ";
        cin >> choice;
        continueCalculations = (choice == 'y' || choice == 'Y');
}

    return 0;
}


// Function to perform basic arithmetic operations
/* Please note that this comes before the main method 
We will see why when we cover functions*/
double performOperation(double a, char op, double b) {
    switch (op) {
        case '+': return a + b; // Addition
        case '-': return a - b; // Subtraction
        case '*': return a * b; // Multiplication
        case '/':   // Division
            if (b != 0) {
                return a / b;
            } else {
                cout << "Error: Division by zero!" << endl;
            return 0;
            }
        case '%':    // Modulus (remainder)
            if (b != 0) {
            return static_cast<int>(a) % static_cast<int>(b);
            } else {
            cout << "Error: Division by zero!" << endl;
            return 0;
            }
        default:
            cout << "Error: Unknown operator!" << endl;
            return 0;
    }
}
