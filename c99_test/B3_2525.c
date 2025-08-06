#include <stdio.h>
#include <string.h>

int main(void) {
    int hour, minute;
    scanf("%d %d", &hour, &minute);
    int working_min;
    scanf("%d", &working_min);
    // printf("hour %d, minute %d, working_min %d\n", hour, minute, working_min);

    int added_min = minute + working_min;
    int added_hour = hour + added_min / 60;
    // printf("added_hour %d, added_min %d\n", added_hour, added_min);
    if (added_hour >= 24) {
        added_hour %= 24;
    }
    added_min %= 60;
    // printf("modified added_min %d\n", added_min);

    printf("%d %d", added_hour, added_min);
    
    return 0;
}

/*
get hour minute
get additional min
add two minutes 
    Div by 60 -> 몫 += hour, 나머지 %
    40 + 80 = 120, 120/60
*/