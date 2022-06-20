#include <stdio.h>
#include <stdlib.h>


int rod_dp(){

    int rod[] = {0,1,4,5,7,9,11,13,13,15,16};

    // 이차원 배열 dp 설정
    int** dp = (int**)malloc(sizeof(int*) * (10+1));
    for (int i = 0; i <= 10; i++) { 
        dp[i] = (int*)malloc(sizeof(int) * i); 
    }

    // 초기값 설정
    

    // dp에 이전 데이터와 이전전 데이터 저장
  
    return 0;
}


int main(){
    printf("\nn = 5  -> %d\n", fibo_dp(5));
    printf("n = 10 -> %d\n\n", fibo_dp(10));
}