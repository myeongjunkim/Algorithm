#include<stdio.h>
#include <stdlib.h>
#include <time.h>

int** get_matrix(int M, int N);
int print_matrix(int** arr, int M, int N);

int** mul_matrix(int** arr1, int arr1_M, int arr1_N, int** arr2, int arr2_N);
// int** mul_strassen()
int mul_strassen(int** arr1,int** arr2);
int main() {
    int** matrix1 = get_matrix(30, 10);
    int** matrix2 = get_matrix(10, 50);

    print_matrix(matrix1, 30,10);
    // print_matrix(matrix2, 10,50);

    // int** multified_matrix = mul_matrix(matrix1, 3,2, matrix2, 5);
    // print_matrix(multified_matrix, 3,5);

    int a = mul_strassen(matrix1, matrix2);

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

int mul_strassen(int** arr1,int** arr2){
    int a11[15][5], a12[15][5], a21[15][5], a22[15][5];
    // split arr1
    for(int i=0; i<30; i++){
        for(int j=0; j<10; j++){
            if(i<15){
                if(j<5){ // a11
                    a11[i][j] = arr1[i][j];
                } else{  //a21
                    a12[i][j-5] = arr1[i][j];
                }
            } else{
                if(j<5){ // a12
                    a21[i-15][j] = arr1[i][j];
                } else{ // a22
                    a22[i-15][j-5] = arr1[i][j];
                }
            }
        }
    }

    int b11[5][25], b12[5][25], b21[5][25], b22[5][25];
    // split arr2
    for(int i=0; i<10; i++){
        for(int j=0; j<50; j++){
            if(i<5){
                if(j<25){ // a11
                    b11[i][j] = arr2[i][j];
                } else{  //a21
                    b12[i][j-25] = arr2[i][j];
                }
            } else{
                if(j<25){ // a12
                    b21[i-5][j] = arr2[i][j];
                } else{ // a22
                    b22[i-5][j-25] = arr2[i][j];
                }
            }
        }
    }

    




    return 0;
}


// int** mul_strassen(int** arr1, int arr1_M, int arr1_N, int** arr2, int arr2_N){
    
//     int** a11 = (int**)malloc(sizeof(int*) * arr1_M/2);
//     for (int i = 0; i < arr1_M/2; i++) {
//         a11[i] = (int*)malloc(sizeof(int) * arr1_N/2);
//     }
//     for(int i=0; i<arr_M/2; i++){
//         for(int j=0; j<arr_N/2; j++){
//                 a11[i][j] = arr1[i][j];
//             }
//         }
//     }

//     int** a12 = (int**)malloc(sizeof(int*) * arr1_M/2);
//     for (int i = 0; i < arr1_M/2; i++) {
//         a12[i] = (int*)malloc(sizeof(int) * arr1_N/2);
//     }
//     for(int i=arr_M/2; i<arr_M; i++){
//         for(int j=0; j<arr_N/2; j++){
//                 a12[i-arr_M/2][j] = arr1[i][j];
//             }
//         }
//     }

//     int** a21 = (int**)malloc(sizeof(int*) * arr1_M/2);
//     for (int i = 0; i < arr1_M/2; i++) {
//         a21[i] = (int*)malloc(sizeof(int) * arr1_N/2);
//     }
//     for(int i=0; i<arr_M/2; i++){
//         for(int j=arr_N/2; j<arr_N; j++){
//                 a21[i][j-arr_N/2] = arr1[i][j];
//             }
//         }
//     }

//     int** a22 = (int**)malloc(sizeof(int*) * arr1_M/2);
//     for (int i = 0; i < arr1_M/2; i++) {
//         a22[i] = (int*)malloc(sizeof(int) * arr1_N/2);
//     }
//     for(int i=arr_M/2; i<arr_M; i++){
//         for(int j=arr_N/2; j<arr_N; j++){
//                 a21[i-arr_M/2][j-arr_N/2] = arr1[i][j];
//             }
//         }
//     }



// }