// Topic: Recursion in C++ - Sum of odd numbers up to n
#include<iostream>
using namespace std;

int sumOdd(int n) {
    if (n <= 0)
        return 0;
    if (n % 2 == 0)
        return sumOdd(n - 1);
    return n + sumOdd(n - 2);
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << "Sum of odd numbers up to " << n << " = " << sumOdd(n);
    return 0;
}