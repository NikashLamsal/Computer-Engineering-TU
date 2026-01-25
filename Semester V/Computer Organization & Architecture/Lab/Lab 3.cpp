// lab 3 : Multiplication of signed binary integers sing booths algorithm

#include <stdio.h>

void asr(int p[] , int q[0] , int n)
{

int temp = p[n-1];
    for (int i = n-1; i > 0; i--) {
        p[i] = p[i-1];
    }
    p[0] = temp;

    temp = q[n-1];
    for (int i = n-1; i > 0; i--) q[i] = q[i-1];
    q[0] = temp;

}







// int add(int A , int P){



// }


// int sub(int A, int P){

// }


// int MUL(long int mpc, long int mpl)
// {
//     int q0 = 0 ;
//     int a = 0000;
//     int n = 4;

//     int x = mpl%10;

//     if (x == 1 && q0== 1 || x == 0 && q0 == 0)
//     {
        
//         // return asr(a , mpl , q0 );
//     }
//     else if( x == 1 && q0 == 0){
        
        
//         return add(a , mpc);

//     }
//     else if( x == 0 && q0 == 1){
        
        
//         return sub(a , mpc);

//     }

// }


int main()
{   
    long int m , q;
    int n;

    int M[n], Q[n], P[n], Q1 = 0;


    printf("Enter the multiplicand : ");
    scanf("%d",&m);
    printf("Enter the Multiplier : ");
    scanf("%d",&q);

    printf("Enter the no of bit : ");
    scanf("%d",&n);


    for (int i = n-1; i >= 0; i--) {
        M[i] = (m >> i) & 1;
        Q[i] = (q >> i) & 1;
        P[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        if (Q[n-1] == 0 && Q1 == 1) {
            for (int j = n-1; j >= 0; j--) {
                P[j] += M[j];
                if (P[j] >= 2) {
                    P[j] -= 2;
                    if (j > 0) P[j-1]++;
                }
            }
        } else if (Q[n-1] == 1 && Q1 == 0) {
            for (int j = n-1; j >= 0; j--) {
                M[j] = !M[j];
            }
            M[0]++;
            for (int j = 0; j < n; j++) {
                P[j] += M[j];
                if (P[j] >= 2) {
                    P[j] -= 2;
                    if (j > 0) P[j-1]++;
                }
            }
            for (int j = n-1; j >= 0; j--) {
                M[j] = !M[j];
            }
            M[0]--;
        }
        Q1 = Q[n-1];
        asr(P, Q, n);
    }

    printf("Product: ");
    for (int i = 0; i < n; i++) printf("%d", P[i]);
    for (int i = 0; i < n; i++) printf("%d", Q[i]);
    printf("\n");

return 0;
}