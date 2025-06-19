//  find the highest digit in a number using recursion
#include <iostream>
using namespace std;

int highestdigit(int n) {
    if (n == 0)
        return 0;
    int digit = n % 10;
    int max = highestdigit(n / 10);
    return (digit > max) ? digit : max;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    
    int result = highestdigit(num);
    cout << "Highest digit: " << result << endl;

    return 0;
}
