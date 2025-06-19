// Topic: Sum of numbers from 1 to N using recursion
#include <iostream>
using namespace std;

int sumUptoN(int n) {
    if (n == 0)
        return 0;
    return n + sumUptoN(n - 1);
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Sum up to " << n << " is: " << sumUptoN(n) << endl;
    return 0;
}
