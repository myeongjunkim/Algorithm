#include<stdio.h>
#include <math.h>

int main() {
    
    printf("\n<satisfying the following equations 2^k <= n>\n\n");    

    int numlist[] = {10, 50, 100};
    for(int i=0; i< sizeof(numlist)/sizeof(int); i++){
        int k = 1;
        while(pow(2,k)<=numlist[i]){
            k++;
        };
        printf("The largest positive integer k is %d\n", k-1);
        
    };
    
}