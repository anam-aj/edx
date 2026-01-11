#include <iostream>

using namespace std;


int main() {
    // Player attributes
    int playerLevel = 3;
    int playerScore = 1250;
    int minimumLevel = 5;
    int minimumScore = 1000;
    bool hasCompleteMap = true;
    // Relational comparisons
    bool levelQualified = playerLevel >= minimumLevel;
    bool scoreQualified = playerScore >= minimumScore;
    cout << "Level qualified: " << (levelQualified ? "Yes" : "No") << endl;
    cout << "Score qualified: " << (scoreQualified ? "Yes" : "No") << endl;
    // Logical combinations
    bool basicAchievement = levelQualified && scoreQualified;
    bool specialAchievement = basicAchievement && hasCompleteMap;
    bool anyQualification = levelQualified || scoreQualified;
    cout << "Basic achievement: " << (basicAchievement ? "Earned" : "Not earned") << endl;
    cout << "Special achievement: " << (specialAchievement ? "Earned" : "Not earned") << endl;
    cout << "Any qualification: " << (anyQualification ? "Yes" : "No") << endl;
    return 0;
}
