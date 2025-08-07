#include <stdio.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void){
    int num1, num2, num3;
    int numbers[3];
    while (1) {
        scanf("%d %d %d", &num1, &num2, &num3);
        if (num1+num2+num3 == 0)
            break;
        
        // Sorting by descending the list. ex) 7 4 3
        numbers[0] = num1;
        numbers[1] = num2;
        numbers[2] = num3;
        for (int i=0; i<3-1; i++){
            for (int j=0; j<3-1-i; j++){
                if (numbers[j] < numbers[j+1]){
                    swap(&numbers[j], &numbers[j+1]);
                }
            }
        }

        // invalid - descending logic..
        if (numbers[1]+numbers[2] <= numbers[0])
            printf("Invalid\n");
        else if (num1 == num2 && num1 == num3)
            printf("Equilateral\n");
        else if (num1 == num2 || num1 == num3 || num2 == num3)
            printf("Isosceles\n");
        else
            printf("Scalene\n");
    }

    return 0;
}

/*
Equilateral, Isosceles, Scalene, Invalid

keep get three length
if 0 0 0, stop

compare
    Equilateral if all same
    Isosceles if only two same
    Scalene if all diff
    Invalid 
*/
