#include <iostream>

int main(void){
    int test_casees;
    std::cin >> test_casees;
    for (int i=0; i<test_casees; i++){
        int num_lines;
        std::cin >> num_lines;

        for (int j=0; j<num_lines; j++){
            std::cout << "#";
        }
        if (num_lines != 1)
            std::cout << std::endl;

            for (int k=0; k<num_lines-2; k++){
                std::cout << "#";
                for (int j=0; j<num_lines-2; j++){
                    std::cout << "J";
                }
                std::cout << "#" << std::endl;
            }

            if (num_lines > 1){
                for (int j=0; j<num_lines; j++){
                    std::cout << "#";
                }
            }

            if (i != test_casees-1)
                std::cout << std::endl << std::endl;
    }
    return 0;
}