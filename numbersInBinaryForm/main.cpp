#include <iostream>
using namespace std;

int printbits(int k){
    int one = 1;
    int size = 8*sizeof(int);
    for(int n=size-2; n >= 0; n--) {
        printf("%d", (k>>n)&one); 
    }
    printf("\n");
    return 0;
}

int main(){
    cout <<printbits(11)<<endl;
    return 0;
}
// OUTPUT:
// @ravikumargrk ➜ /workspaces/puzzles/numbersInBinaryForm/C++ (main) $ g++ main.cpp
// @ravikumargrk ➜ /workspaces/puzzles/numbersInBinaryForm/C++ (main) $ ./a.out
// 0000000000000000000000000001011