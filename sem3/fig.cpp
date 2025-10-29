#include <graphics.h>
#include <conio.h>
#include <iostream>
using namespace std;

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");  // Initialize graphics mode

    setcolor(RED);
    rectangle(100, 100, 300, 200);

    setcolor(BLUE);
    circle(200, 150, 50);

    setcolor(GREEN);
    line(50, 50, 350, 250);

    getch();       // Wait for key press
    closegraph();  // Close graphics mode
    return 0;
}
