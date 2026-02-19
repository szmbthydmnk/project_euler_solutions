#include <cmath>

int sum_of_number_digit_powers(int Number, int Power){

    int NumberTemp = int(Number);
    int sum = 0;

    while (NumberTemp > 0){
        int digit = NumberTemp % 10;
        sum += pow(digit, Power);
        NumberTemp /= 10;
    }

    return sum;
}