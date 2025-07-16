#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; ++i) { 
        bool swapped = false;

        for (int j = 0; j < n - i - 1; ++j) { 
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        if (!swapped) {
            break; 
        }
    }
}

int main() {
    int arr[] = {5, 3, 7, 2, 8};
    int n = sizeof(arr)/sizeof(arr[0]);

    bubbleSort(arr, n);

    std::cout << "Sorted array: ";
    for (int i = 0; i < n; ++i) {
        std::cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}