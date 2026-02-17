#include <stdio.h>
#include <math.h>

// Function to convert decimal to binary
void decimalToBinary(int num, int bin[], int n) {
    int i;
    for (i = n - 1; i >= 0; i--) {
        bin[i] = num % 2;
        num = num / 2;
    }
}

// Function to convert binary array to decimal
int binaryToDecimal(int bin[], int n) {
    int i, decimal = 0;
    for (i = 0; i < n; i++) {
        decimal = decimal * 2 + bin[i];
    }
    return decimal;
}

// Function to print binary number
void printBinary(int bin[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%d", bin[i]);
    }
}

// Restoring Division Function
void restoringDivision(int Q[], int M[], int n) {
    int A[20] = {0};  // Accumulator initialized to 0
    int i, j;

    for (i = 0; i < n; i++) {

        // Left shift (A,Q)
        for (j = 0; j < n - 1; j++)
            A[j] = A[j + 1];
        A[n - 1] = Q[0];

        for (j = 0; j < n - 1; j++)
            Q[j] = Q[j + 1];
        Q[n - 1] = 0;

        // A = A - M
        int decimalA = binaryToDecimal(A, n);
        int decimalM = binaryToDecimal(M, n);

        decimalA = decimalA - decimalM;

        // Convert result back to binary
        decimalToBinary(decimalA, A, n);

        // Check if A < 0
        if (decimalA < 0) {
            // Restore A
            decimalA = decimalA + decimalM;
            decimalToBinary(decimalA, A, n);
            Q[n - 1] = 0;
        } else {
            Q[n - 1] = 1;
        }
    }
    
    printf("\nQuotient = ");
    printBinary(Q, n);

    printf("\nRemainder = ");
    printBinary(A, n);
}

int main() {
    int dividend, divisor, n;
    int Q[20], M[20];

    printf("Enter number of bits: ");
    scanf("%d", &n);

    printf("Enter dividend: ");
    scanf("%d", &dividend);

    printf("Enter divisor: ");
    scanf("%d", &divisor);

    if (divisor == 0) {
        printf("Division by zero error!\n");
        return 0;
    }

    decimalToBinary(dividend, Q, n);
    decimalToBinary(divisor, M, n);

    restoringDivision(Q, M, n);

    return 0;
}
