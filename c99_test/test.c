#include <stdio.h>

int factorial_calculator(int n){
    int result;
    // 1. escape conditon
    if (n == 1){
        return 1;
    }
    // 2. recursive
    result = n * factorial_calculator(n-1);

    return result;
}

void fibo_calculator(int current, int target, int* arr){
    // 2. recursive
    arr[current] = arr[current-2] + arr[current-1];
    // 1. escape
    if (current == target) {
        return;
    }
    fibo_calculator(current+1, target, arr);
}

int main(void){
    int factorial_n;
    printf("1. Factorial : ");
    scanf("%d", &factorial_n);
    printf("%d! = %d\n\n", factorial_n, factorial_calculator(factorial_n)); 

    int fibo_target;
    int fibo_current = 2;
    printf("2. Fibo(n>2) : ");
    scanf("%d", &fibo_target);
    int fibo_arr[fibo_target];
    fibo_arr[0] = 0;
    fibo_arr[1] = 1;
    fibo_calculator(fibo_current, fibo_target-1, fibo_arr);
    for (int i=0; i<fibo_target; i++){
        printf("%d ", fibo_arr[i]);
    }
    printf("\n");

    return 0;
}