#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX(a, b) ( (a > b) ? a : b );


int rod_dp(int price[], int n, int dp[], int s[]){
    
    int max_p = INT_MIN;
    int new_max;

    if (dp[n] >=0) return dp[n];
    if (n==0) max_p=0;

    // dp에 데이터 저장
    for(int i=1; i<=n; i++){
        new_max = MAX(max_p, price[i] + rod_dp(price, n-i, dp, s));
        if (new_max > max_p){
            s[n] = i;
            max_p = new_max;
        }

    }
    dp[n] = max_p;
    return max_p;
}


int main(){

    // 가격 선언
    int price[] = {0,1,4,5,7,9,11,13,13,15,16};

    // dp 초기값 설정
    int dp[10+1];
    int s[10+1];
    for(int i=0; i<=10; i++){
        dp[i] = INT_MIN;
    }

    // dp, s 에 해 저장
    rod_dp(price, 10, dp, s);

    // 결과 출력
    int n;
    for(int i=1; i<=10; i++){
        printf("maximum price(length %2d) : %2d  => ", i, dp[i]);
        n = i;
        while(n>0){
            printf("%d ", s[n]);
            n -= s[n];
        }
        printf("\n");
    }
}