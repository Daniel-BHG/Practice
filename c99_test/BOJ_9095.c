#include <stdio.h>

// functionality : 
int recursive_summing(int current_sum, int target){
    // 1. if match, return 1
    if (current_sum == target){
        return 1;
    }
    
    // 2. if exceed, return 0
    if (current_sum > target){
        return 0;
    }

    // 3. if lower
    int count = 0;
    count += recursive_summing(current_sum+3, target);
    count += recursive_summing(current_sum+2, target);
    count += recursive_summing(current_sum+1, target);

    return count;
}

int main(void){
    int test_cases;
    scanf("%d", &test_cases);

    // running test_cases
    for (int i=0; i<test_cases; i++){
        int target;
        scanf("%d", &target);
        printf("%d\n", recursive_summing(0, target));
    }

    return 0;
}