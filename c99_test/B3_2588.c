#include <stdio.h>

int main(void){
    int num1, num2;
    scanf("%d %d", &num1, &num2);

    // setting all separate numbers for num2
    int num2_100 = num2/100;
    int num2_10 = (num2 - (num2_100*100)) / 10;
    int num2_1 = (num2 - num2_100*100 - num2_10*10);

    int num3 = num1 * num2_1;
    printf("%d\n", num3);
    int num4 = num1 * num2_10;
    printf("%d\n", num4);
    int num5 = num1 * num2_100;
    printf("%d\n", num5);
    int num6 = num3 + num4*10 + num5*100;
    printf("%d\n", num6);

    return 0;
}

/*
input two three-digit int
utilize div
    be aware of the 자리수
354 / 100 = 3
(354 - 300) / 10 = 5
(354 - 300 - 50) = 4
*/