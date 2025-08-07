#include <iostream>
#include <vector>
#include <algorithm>
// using namespace std;

int main(void) {
    int num1, num2, num3;
    std::vector<int> numbers(3);
    while (1) {
        std::cin >> num1 >> num2 >> num3;
        if (num1+num2+num3 == 0)
            break;

        numbers[0] = num1;
        numbers[1] = num2;
        numbers[2] = num3;

        std::sort(numbers.begin(), numbers.end(), [](int a, int b) {return a > b;});

        // invalid - descending logic..
        if (numbers[1]+numbers[2] <= numbers[0])
            std::cout << "Invalid" << std::endl;
        else if (num1 == num2 && num1 == num3)
            std::cout << "Equilateral" << std::endl;
        else if (num1 == num2 || num1 == num3 || num2 == num3)
            std::cout << "Isosceles" << std::endl;
        else
            std::cout << "Scalene" << std::endl;
    }
    
    return 0;
}