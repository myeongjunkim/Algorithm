#include<stdio.h>
#include <stdlib.h>
#include <time.h>

int** get_matrix(int M, int N);
int print_matrix(int** arr, int M, int N);

int** mul_matrix(int** arr1, int arr1_M, int arr1_N, int** arr2, int arr2_N);

int main() {
    int** matrix1 = get_matrix(3, 2);
    int** matrix2 = get_matrix(2, 5);

    print_matrix(matrix1, 3,2);
    print_matrix(matrix2, 2,5);

    int** multified_matrix = mul_matrix(matrix1, 3,2, matrix2, 5);

    print_matrix(multified_matrix, 3,5);




    return 0;
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

int** mul_matrix(int** arr1, int arr1_M, int arr1_N, int** arr2, int arr2_N){
    
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
