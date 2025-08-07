#include <stdio.h>

#define ROWS 9
#define COLS 9

int main(void){
    int data[ROWS][COLS];
    // get datas
    for (int i=0; i<ROWS; i++){
        for (int j=0; j<COLS; j++){
            scanf("%d", &data[i][j]);
        }
    }

    int max_num = 0;
    int max_row, max_col;
    for (int i=0; i<ROWS; i++){
        for (int j=0; j<COLS; j++){
            if (data[i][j] >= max_num){
                max_num = data[i][j];
                max_row = i;
                max_col = j;
            }
        }
    }
    // be aware of the pos 
    printf("%d\n%d %d", max_num, max_row+1, max_col+1);
    return 0;
}

/*
how to check the max numb
check the all components and 
*/