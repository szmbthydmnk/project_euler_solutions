#include <iostream>
#include <cmath>
#include "sum_of_number_digit_powers.h"

using namespace std;

int main(){
    int NumberOfDigits = 5;
    int Sum = 0;
    for(int NumInd = 2; NumInd <= (pow(10, NumberOfDigits+1) - 1); NumInd++){
        int Number_from_powers = sum_of_number_digit_powers(NumInd, NumberOfDigits);
        
        // cout<< "# " << NumInd << "\t Powersum " << Number_from_powers <<endl;

        if (Number_from_powers == NumInd){
            cout<< "# " << Number_from_powers <<endl;
            Sum += Number_from_powers;
        }
    }
    cout<< "The sum is: " << Sum << endl;
    return 0;
}