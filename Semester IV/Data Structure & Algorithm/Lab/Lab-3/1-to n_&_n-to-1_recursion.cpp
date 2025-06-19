#include <iostream>
using namespace std;

class rec {
public:
    void printHead(int n) {
        if (n < 1) {
            return;
        }
        printHead(n - 1);
        cout << "num: " << n << endl;
    }

    void printTail(int n) {
        if (n < 1) {
            return;
        }
        cout << "num: " << n << endl;
        printTail(n - 1);
    }
};

int main() {
    rec obj; 
    int n;

    cout << "Enter the number to print from: " << endl;
    cin >> n;

    if (n < 1) {
        cout << "Please enter a positive number." << endl;
        return 0;
    }

    cout << "\nUsing Head Recursion:" << endl;
    obj.printHead(n);

    cout << "\nUsing Tail Recursion:" << endl;
    obj.printTail(n);

    return 0;
}