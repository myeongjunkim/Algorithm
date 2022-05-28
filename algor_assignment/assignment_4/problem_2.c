#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MIN(A, B) ((A)>(B)?(B):(A))


int** mul_matrix(int** arr1, int** arr2, int arr1_M, int arr1_N, int arr2_N){
    
    int** result_arr = (int**)malloc(sizeof(int*) * arr1_M);
    for (int i = 0; i < arr1_M; i++) { 
        result_arr[i] = (int*)malloc(sizeof(int) * arr2_N); 
    }
    
    for(int i=0; i<arr1_M; i++){
        for(int k=0; k<arr2_N; k++){
            int sum = 0;
            for(int j=0; j<arr1_N; j++){
                sum += arr1[i][j]*arr2[j][k];
            }
            result_arr[i][k] = sum;
        }
    }

    return result_arr;
}

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


int matrix_product_dp(int* size, int N, int** dp, int** k_index){ // 행렬 차수 배열 size, 행렬 개수 N

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
                    // k 인덱스 저장
                    if (min_case == case_m) k_index[i][i+gap] = k;
                }
                dp[i][i+gap] = min_case;
            }
            
        }
    }

    return k_index[1][N];
}



int** optimal_product(int** matrix[], int** k_index, int* size, int start, int end){
    
    if (end == start) return matrix[start-1];
    if (end - start == 1) return mul_matrix(matrix[start-1], matrix[end-1], size[start-1], size[start], size[end]);

    int k = k_index[start][end];
    printf("\n(matrix %d~%d) x matix (%d~%d)\n", start, k, k+1, end);
    int** matrix_1 = optimal_product(matrix, k_index, size, start, k);

    int** matrix_2 = optimal_product(matrix, k_index, size, k+1, end);


    return mul_matrix(matrix_1, matrix_2, size[start-1], size[k], size[end]);

}


int main(){
    int size[] = {5, 3, 7, 10}; int N = 3;

    // 랜덤 matrix 생성
    int** matrix[N];
    for(int i=0; i<N; i++){
        matrix[i] = get_matrix(size[i], size[i+1]);
    }

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

    // dp, k_index 구하기
    int computations_n = matrix_product_dp(size, N, dp, k_index);

    // 순서에 맞게 주어진 k_index를 활용하여 행렬 곱셈
    int** result_arr = optimal_product(matrix, k_index, size, 1, N);

    // 출력
    for(int i=0; i<N; i++){
        printf("\n<  matrix_%d (%d x %d) >\n\n", i+1, size[i], size[i+1]);
        print_matrix(matrix[i], size[i], size[i+1]);
    }

    printf("\n< result matrix >\n\n");
    print_matrix(result_arr, size[0], size[N]);

    printf("computations : %d\n\n", dp[1][N]);
}