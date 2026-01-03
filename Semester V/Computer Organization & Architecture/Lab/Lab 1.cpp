#include <stdio.h>

int main()
{
    int num1, num2, t1, t2, a[5];
    int sum, c = 0;
    int i = 4;

    printf("enter two numbers");
    scanf("%d %d", &num1, &num2);

    do
    {
        t1 = num1 % 10;
        t2 = num2 % 10;

        sum = (t1 + t2 + c) % 2;
        c = (t1 + t2 + c) / 2;

        a[i] = sum;

        num1 = num1 / 10;
        num2 = num2 / 10;

        i--;
    }
    while (i > 0);

    a[i] = c;

    for (i = 0; i <= 4; i++)
    {
        printf("%d", a[i]);
    }

    return 0;
}
