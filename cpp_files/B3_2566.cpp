#include <iostream>
#include <vector>

const int ROWS = 9;
const int COLS = 9;

int main(void){
    std::vector<std::vector<int>> data(ROWS, std::vector<int>(COLS));
    for (int i=0; i<ROWS; i++){
        for (int j=0; j<COLS; j++){
            std::cin >> data[i][j];
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
    std::cout << max_num << std::endl << max_row+1 << " " << max_col+1;
    return 0;
}