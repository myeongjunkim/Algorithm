#include<stdio.h>
#include <stdlib.h>
#include <time.h>

int* get_random_arr(int N){
    srand(time(NULL));
    int* arr = malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++){
        arr[i] = rand()%N;
    }
    return arr;
}

int* get_worst_arr(int N){
    int* arr = malloc(sizeof(int) * N);
    for(int i=0; i<N; i++){
        arr[i] = N-1-i;
    }
    return arr;
}

void copy_arr(int* arr, int* copy_arr, int n) {
	for (int i = 0; i < n; i++) {
		copy_arr[i] = arr[i];
	}
}

void print_arr(int* arr, int N){
    printf("행렬 출력\n\n");
    for(int i=0; i<N; i++){
        printf("%d번째 : %d\n", i, arr[i]);
    }
}

void compare_arr(int* arr, int* arr2, int N){
    printf("\n행렬 출력\n\n");
    for(int i=0; i<N; i++){
        printf("%5d번째 : %5d -> %5d\n", i, arr[i], arr2[i]);
    }
}

void bubble_sort(int* arr, int N){
    for(int i=0; i<N; i++){
        for(int j=N-1; j>i; j--){
            if(arr[j]<arr[j-1]){
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
        }
    }
}      


int main() {

    // 난수 배열 생성
    int* r_arr_1000 = get_random_arr(1000);
    int* r_arr_5000 = get_random_arr(5000);
    int* r_arr_10000 = get_random_arr(10000);

    // worst 배열 생성
    int* w_arr_1000 = get_worst_arr(1000);
    int* w_arr_5000 = get_worst_arr(5000);
    int* w_arr_10000 = get_worst_arr(10000);

    //버블 정렬
    int r_bubble_1000[1000];
    int r_bubble_5000[5000];
    int r_bubble_10000[10000];
    copy_arr(r_arr_1000, r_bubble_1000, 1000);
    copy_arr(r_arr_5000, r_bubble_5000, 5000);
    copy_arr(r_arr_10000, r_bubble_10000, 10000);

    bubble_sort(r_bubble_1000, 1000);
    compare_arr(r_arr_1000, r_bubble_1000, 1000);


}