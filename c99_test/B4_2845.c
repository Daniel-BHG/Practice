#include <stdio.h>
#include <string.h>

int main(void) {
    int L, P;
    scanf("%d %d", &L, &P);
    int exact_num = L*P;

    int arr[5];
    for (int i=0; i<5; i++)
        scanf("%d", &arr[i]);
    
    for (int j=0; j<5; j++){
        if (j != 4)
            printf("%d ", arr[j]-exact_num);
        else
            printf("%d", arr[j]-exact_num);
    }
    return 0;
}

/*
get L, P and calculate the correct num = L * P
get five nums by list
compare the components
    if correct num < list, substrate with +
    if not, substrate with -
*/