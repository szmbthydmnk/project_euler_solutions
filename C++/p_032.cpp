/*
Project euler 32. problem
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 
5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity,39 x 186 = 7254, containing multiplicand, multiplier, and product is
1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
 */

#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

bool HasPandigitalProduct(int a){
    string NumberString;
    string NumberStringTemp;

    for(int i = 1; i <= (sqrt(a) + 1); i++){
        if(a % i == 0){
            NumberString = to_string(i) + to_string(a) + to_string(a / i);
            sort(NumberString.begin(), NumberString.end());
            if( NumberString == "123456789"){
                return true;
            }
        }
    }
    return false;
}

int main(){
    int NoPandigitals = 0;
    for(int i = 1; i < 100000; i++){
        if(HasPandigitalProduct(i) == true){
            NoPandigitals += i;
        }
    }
    cout<<NoPandigitals<<endl;
    return 0;
}

