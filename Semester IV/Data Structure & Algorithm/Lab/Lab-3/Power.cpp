// Topic: Power calculation using recursion (a^b)

#include <iostream>
using namespace std;

int power(int base, int exponent) {
    if (exponent == 0)
        return 1;
    return base * power(base, exponent - 1);
}

int main() {
    int a, b;
    cout << "Enter base and exponent: ";
    cin >> a >> b;
    cout << a << "^" << b << " = " << power(a, b) << endl;
    return 0;
}