#include <iostream>

using namespace std;

int euler28(int GridSize){
    int Sum = 1;
    for(int sumInd = 3; sumInd <= GridSize + 1; sumInd += 2){
        if(sumInd % 2 == 1){
            Sum += 6 * (1 - sumInd) + 4 * sumInd * sumInd;
        }
        /* cout <<"N = "<< sumInd << "\t sum = " << Sum << endl; */
    }
    return Sum;
}

int main(){
    int N = 1001;
    int Sum;
    Sum = euler28(N);
    printf("The sum is Sum = %d ", Sum);
    return 0;
}
