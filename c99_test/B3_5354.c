#include <stdio.h>

int main(void){
    int test_cases;
    scanf("%d", &test_cases);
    for (int i=0; i<test_cases; i++){
        int num_lines;
        scanf("%d", &num_lines);
        
        // first line
        for (int j=0; j<num_lines; j++){
            printf("#");
        }
        if (num_lines != 1)
            printf("\n");

        // body line
        for (int k=0; k<num_lines-2; k++){
            printf("#");
            for (int j=0; j<num_lines-2; j++){
                printf("J");
            }
            printf("#\n");
        }

        // last line
        if (num_lines > 1){
            for (int j=0; j<num_lines; j++){
                printf("#");
            }
        }

        if (i != test_cases-1)
            // \n for next case
            printf("\n\n");
    }

    return 0;
}

/*
num_lines = 5
#####
#JJJ#
#JJJ#
#JJJ#
#####

num_lines = 4
####
#JJ#
#JJ#
####

what if num_lines = 1, 2
num_lines = 2
##
##

num_lines = 1
#
*/