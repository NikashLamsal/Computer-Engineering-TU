// Multiplication of two unsigned integer binary numbers by partial product method .

#include <stdio.h>

int binaryProduct(int, int);

void mul(long int bin1, long int bin2)
{
 long int multiply = 0; // accumulator or partial product P
 int digit, factor = 1; // digit stores the right most bit
 while (bin2 != 0)
 {
		digit = bin2 % 10;

		if (digit == 1)
		{
			bin1 = bin1 * factor;
			multiply = binaryProduct(bin1, multiply);
		}
		else
			bin1 = bin1 * factor;
		printf("\n");
		printf("%ld", bin1);

		bin2 = bin2 / 10;
		factor = 10;
 }
 printf("Product of two binary numbers: %ld", multiply);
}

int binaryProduct(int binary1, int binary2)
{
 int i = 0, remainder = 0, sum[20];
 int binaryprod = 0;
 printf("\n%d \t%d \n", binary1, binary2);
 if (binary2 == 0 )
 {
    binaryprod = binary1;
 }
 else 
 {
 while (binary1 != 0 || binary2 != 0)
 {
		sum[i++] = (binary1 % 10 + binary2 % 10 + remainder) % 2; // make value between 0 and 1

		remainder = (binary1 % 10 + binary2 % 10 + remainder) / 2;
		binary1 = binary1 / 10;
		binary2 = binary2 / 10;
 }

 if (remainder != 0)
		sum[i++] = remainder;
 --i;
 while (i >= 0)
		binaryprod = binaryprod * 10 + sum[i--];
 }
 printf("partialProduct: %d \n", binaryprod);
 return binaryprod;
}


int main()
{
 long int binary1, binary2;
 printf("Enter the first binary number: ");
 scanf("%ld", &binary1);
 printf("Enter the second binary number: ");
 scanf("%ld", &binary2);
 mul(binary1, binary2);
 return 0;
}