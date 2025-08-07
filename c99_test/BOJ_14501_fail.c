#include <stdio.h>

int total_days;
int T[16];
int P[16];

int max(int a, int b){
    return (a > b) ? a : b;
}

int find_max_profit(int start_day){
    // 1. escape condition
    if (start_day > total_days) {
        // printf("DE")
        return 0;
    }

    // key point - max profit - which day will "choose"
    // 2-1. right after the day
    int profit_if_work = 0;
    if (start_day + T[start_day] <= total_days){
        // printf("1) DEBUG-WORK: Day %d -> %d, Current profit %d\n", start_day, start_day+T[start_day], profit_if_work);
        profit_if_work +=  P[start_day] + find_max_profit(start_day + T[start_day]);
    }

    // 2-2. not right after the day
    // printf("2) DEBUG-SKIP: At Day %d, Current profit %d\n", start_day, profit_if_work);
    int profit_if_skip = find_max_profit(start_day+1);
    // printf("3) DEBUG: return profit-skip %d\n", profit_if_skip);
    return max(profit_if_work, profit_if_skip);
}

int main(){
    scanf("%d", &total_days);
    for (int i=1; i<=total_days; i++){
        scanf("%d %d", &T[i], &P[i]);
    }

    printf("%d", find_max_profit(1));
    return 0;
}