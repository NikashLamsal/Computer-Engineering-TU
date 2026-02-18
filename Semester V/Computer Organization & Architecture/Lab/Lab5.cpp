#include <stdio.h>

void decimalToBinary(int num, int bin[], int n) {
    for (int i = n - 1; i >= 0; i--) {
        bin[i] = num % 2;
        num /= 2;
    }
}

int binaryToDecimal(int bin[], int n) {
    int decimal = 0;
    for (int i = 0; i < n; i++)
        decimal = decimal * 2 + bin[i];
    return decimal;
}

void printBinary(int bin[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d", bin[i]);
}

void add(int A[], int M[], int n) {
    int carry = 0;
    for (int i = n - 1; i >= 0; i--) {
        int sum = A[i] + M[i] + carry;
        A[i] = sum % 2;
        carry = sum / 2;
    }
}

void subtract(int A[], int M[], int n) {
    int M_comp[20];
    int carry = 1;

    for (int i = 0; i < n; i++)
        M_comp[i] = 1 - M[i];

    for (int i = n - 1; i >= 0; i--) {
        int sum = M_comp[i] + carry;
        M_comp[i] = sum % 2;
        carry = sum / 2;
    }

    add(A, M_comp, n);
}

int isNegative(int A[]) {
    return A[0];
}

void restoringDivision(int Q[], int M[], int n) {
    int A[20] = {0};

    for (int i = 0; i < n; i++) {

        for (int j = 0; j < n - 1; j++)
            A[j] = A[j + 1];
        A[n - 1] = Q[0];

        for (int j = 0; j < n - 1; j++)
            Q[j] = Q[j + 1];
        Q[n - 1] = 0;

        subtract(A, M, n);

        if (isNegative(A)) {
            add(A, M, n);
            Q[n - 1] = 0;
        } else {
            Q[n - 1] = 1;
        }

        printf("\nStep %d:", i + 1);
        printf("\nA = "); printBinary(A, n);
        printf("\nQ = "); printBinary(Q, n);
        printf("\n");
    }

    printf("\nFinal Result:");
    printf("\nQuotient  = ");
    printBinary(Q, n);

    printf("\nRemainder = ");
    printBinary(A, n);

    printf("\n\nDecimal Quotient  = %d", binaryToDecimal(Q, n));
    printf("\nDecimal Remainder = %d\n", binaryToDecimal(A, n));
}

int main() {
    int dividend, divisor, n;
    int Q[20], M[20];

    printf("Enter number of bits: ");
    scanf("%d", &n);

    printf("Enter dividend (positive only): ");
    scanf("%d", &dividend);

    printf("Enter divisor (positive only): ");
    scanf("%d", &divisor);

    if (divisor == 0) {
        printf("Division by zero error!\n");
        return 0;
    }

    if (dividend < 0 || divisor < 0) {
        printf("Only non-negative integers allowed!\n");
        return 0;
    }

    if (dividend >= (1 << n) || divisor >= (1 << n)) {
        printf("Numbers exceed %d-bit limit!\n", n);
        return 0;
    }

    decimalToBinary(dividend, Q, n);
    decimalToBinary(divisor, M, n);

    restoringDivision(Q, M, n);

    return 0;
}