#include<iostream>

using namespace std;


class Calc{
    public:
    int num1,num2;
    void doMath(){
        num1 = 10; num2 = 20;
        int result = num1 + num2;
        cout << "result is " << result << endl;
        if(result > 25){
            cout << "big number" << endl;
        }else{
            cout << "small number" << endl;
        }
    }
};


int main(){
    Calc c;
    c.doMath();
    return 0;
}
