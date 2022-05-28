#include <stdio.h>
#include <stdlib.h>


int fibo_dp(int N){

    int** dp = (int**)malloc(sizeof(int*) * (N+1));
    for (int i = 0; i <= N; i++) { 
        dp[i] = (int*)malloc(sizeof(int) * 2); 
    }

    // 초기값 설정
    dp[0][0] = 0; dp[0][1] = 0;
    dp[1][0] = 0; dp[1][1] = 1;

    // dp에 이전 데이터와 이전전 데이터 저장
    for(int i=2; i<=N; i++){
        dp[i][0] = dp[i-1][0] + dp[i-1][1];
        dp[i][1] = dp[i-2][0] + dp[i-2][1];
    }

    return dp[N][0] + dp[N][1];
}


int main(){
    printf("n = 5  -> %d\n", fibo_dp(5));
    printf("n = 10 -> %d\n", fibo_dp(10));
}