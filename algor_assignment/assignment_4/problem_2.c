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


int matrix_product_dp(int* size, int N){

    int** dp = (int**)malloc(sizeof(int*) * (N+1));
    for (int i = 0; i <= N; i++) { 
        dp[i] = (int*)malloc(sizeof(int) * 2); 
    }


}

int main(){

}