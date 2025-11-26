#include <iostream>
#include <iomanip>  // needed for setw

using namespace std;

int main() {
    cout << setw(10) << 42 << "\n";
    cout << setw(10) << "HiHELLOASDASD" << "\n";
    cout << setprecision(3) << 123.456 << endl;   // prints 123
    cout << fixed << setprecision(3) << 123.456 << endl;  // prints 123.456


    return 0;
}
