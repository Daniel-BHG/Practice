#include <stdio.h>

int main(void) {
    int num; // 5
    scanf("%d", &num);

    for (int i = 1; i < num+1; i++){ // i = 1 2 3 4 5
        for (int j = num-i; j > 0; j--){ // j = 4 3 2 1 0
            printf(" ");
        }
        for (int k = 0; k < i; k++) { // count(k) = 1ea 2ea 3ea 4ea 5ea
            printf("*");
        }
        printf("\n");
    }
    return 0;
}