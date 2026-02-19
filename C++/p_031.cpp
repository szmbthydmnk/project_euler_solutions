/*In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
*/


#include <iostream>
#include <vector>

using namespace std;

int main(){
    int PenceAmount = 200;
    auto Coins      = {1, 2, 5, 10, 20, 50, 100, 200};
    vector<long> Ways(PenceAmount + 2, 0);
    Ways[1] = 1;
    for(auto CoinInd : Coins){
        for(int CountingInd = CoinInd; CountingInd <= (PenceAmount); ++ CountingInd){
            Ways[CountingInd + 1] += Ways[CountingInd + 1 - CoinInd];
        }
    }
    cout <<" Number of ways 2 pounds can be added is "<< Ways[PenceAmount + 1] << endl;
    return 0;
}