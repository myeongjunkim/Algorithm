#include<stdio.h>
#include <stdlib.h> 

int** pairSum(int arr[], int N, int target_sum, int* result_len);

int main() {
    int arr[] = {2, 4, 3, 5, 6, -2, 4, 7, 8, 9};
    int arr_len = sizeof(arr)/sizeof(int);
    int target_sum = 7;
    int result_len;
    int** result_arr = pairSum(arr, arr_len, target_sum, &result_len);
    
    for(int i=0; i<result_len; i++){
        if(result_arr[i][1]<0){
            printf("%d%d ", result_arr[i][0],result_arr[i][1]);
        } else{
            printf("%d+%d ", result_arr[i][0],result_arr[i][1]);
        }
    }
    printf("\n");
    
}

int** pairSum(int arr[], int N, int target_sum, int* result_len){
    
    int result_arr_len = N*(N-1)/2;
    int** result_arr = (int**)malloc(sizeof(int*) * result_arr_len);
    for (int i = 0; i < result_arr_len; i++) { 
        result_arr[i] = (int*)malloc(sizeof(int) * 2); 
    }
    
    int top = 0;
    for(int i=0; i<N; i++){
        for(int j=i+1; j<N; j++){
            if(arr[i]+arr[j] == target_sum){
                result_arr[top][0] = arr[i];
                result_arr[top][1] = arr[j];
                // printf("%d, %d\n", result_arr[top][0], result_arr[top][1]);
                top++;
            }
        }
    }

    *result_len = top;
    return result_arr;
}
