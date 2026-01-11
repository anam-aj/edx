#include <iostream>
using namespace std;
int main() {
    // Player statistics
    int baseScore = 85;
    int bonusPoints = 15;
    int timeBonus = 10;
    // Basic calculations
    int totalScore = baseScore + bonusPoints + timeBonus;
    cout << "Total Score: " << totalScore << endl;
    // Division and modulus examples
    int averageScore = totalScore / 3;  //Integer division
    int remainder = totalScore % 10;    // Remainder when divided by 10
    cout << "Average per section: " << averageScore << endl;
    cout << "Score remainder: " << remainder << endl;
    return 0;
}
