#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MIN(A, B) ((A)>(B)?(B):(A))


int** get_matrix(int M, int N){
    srand(time(NULL));
    int** result_arr = (int**)malloc(sizeof(int*) * M);
    for (int i = 0; i < M; i++) { 
        result_arr[i] = (int*)malloc(sizeof(int) * N); 
    }

	for (int i = 0; i< M; i++) {
        for (int j=0; j<N; j++) {
            result_arr[i][j] = rand()%9+1;
        }
	}

    return result_arr;
}

int print_matrix(int** arr, int M, int N){
    for(int i=0; i <M; i++){
        for(int j=0; j<N; j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}


int matrix_product_dp(int* size, int N){ // 행렬 차수 배열 size, 행렬 개수 N

    // N-1 이 행렬의 개수
    // 1~N-1 까지 곱을 저장
    int** dp = (int**)malloc(sizeof(int*) * (N+1));
    for (int i = 0; i < N+1; i++) { 
        dp[i] = (int*)malloc(sizeof(int) * (N+1)); 
    }

    // 각 레벨에서 k값 저장소(어디서 끊겼는지)
    int** k_index = (int**)malloc(sizeof(int*) * (N+1));
    for (int i = 0; i < N+1; i++) { 
        k_index[i] = (int*)malloc(sizeof(int) * (N+1)); 
    }

    for(int gap=0; gap<N; gap++){
        for(int i=1; i<=N-gap; i++){
            if (gap == 0) {
                dp[i][i+gap] = 0;
                k_index[i][i+gap] = i;
            }
            else{
                int case_m; int min_case;
                for(int k=i; k<i+gap; k++){
                    case_m = dp[i][k] + dp[k+1][i+gap] + size[i-1]*size[k]*size[i+gap];
                    if (k == i) min_case = case_m;
                    else min_case = MIN(min_case, case_m);
                }
                dp[i][i+gap] = min_case;
            }
            
        }
    }

    print_matrix(dp, N+1, N+1);

    return dp[1][N];


}

int main(){
    int size[] = {20, 1, 30, 10, 10}; int N = 4;
    matrix_product_dp(size, N);
}