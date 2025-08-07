/*
1~9 : 1 * 9ea
10~99 : 2 * 90ea
100~999 : 3 * 900ea
1000~9999 : 4 * 9000ea
...
10,000,000~99,999,999 : 90,000,000ea
100,000,000 : 1ea

num = 99999
if substrated_num > 0
num(99999) - 9 - 90 - 900

ex) 1002
1~9
10~99
100~999
1000~1002

*/

#include <stdio.h>
#include <math.h>

int cnt = 0;

int counter(int N, int multiplier){
    // 1. escape condition. 1004 < 1000, 5 < 10. 753 - (53=753%100) - 100. 5 - (5%10^0) - 10^0
    if (N < (int)pow(10, multiplier)){
        int residue = N - (N % ((int)pow(10, multiplier-1))) - (int)pow(10, multiplier-1);
    }
//--------------------------------------------------------------------------------------------
    // 2. recursive for *10
    // 753 - 9 - 90 - 900 ...
    int if_possible_recursive = (N - (int)pow(10, multiplier+1)); // 753 - 100 or 753 - 1000
    int updated_N = (N - (int)pow(10, multiplier)*9); // 753 - 90
    if (if_possible_recursive > 0){
        cnt += (multiplier+1)*9 + counter(updated_N-((int)pow(10,0)*9), multiplier+1);
    }
    else { // 753 - 1000 < 0. for the residues
        // 1002 - 9 - 90 - 900 ... recursively
        N - ()
    }
}

int main(){
    int num;
    scanf("%d", &num);
    counter(num, 0);
    
    
    return 0;
}