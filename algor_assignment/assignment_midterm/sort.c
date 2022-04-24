#include<stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// method about sort
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


// sort algorithm
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

void insert_sort(int* arr, int N){
    for(int i=1; i<N; i++){
        int target = arr[i]; int j;
        for(j=i-1; j>=0; j--){
            if(target < arr[j]){
                arr[j+1] = arr[j];
            } else break;
        }
        arr[j+1] = target;
    }
}

void merge_sort(int* arr, int* sorted, int left, int right){
    int mid = (left+right)/2;
    if(left<right){
        merge_sort(arr, sorted, left, mid);
        merge_sort(arr, sorted, mid+1, right);
    }
    int i=left; int j=mid+1; int k=left;
    while(i<=mid && j<= right){
        if(arr[i]<arr[j]){
            sorted[k] = arr[i];
            i++;
        } else{
            sorted[k] = arr[j];
            j++;
        }
        k++;
    }
}



void radix_sort(int* arr, int N){
    int* sorted = malloc(sizeof(int) * N);
    // 최대 자리수 구함
    int max = arr[0];
    for(int i=1; i<N; i++){
        if(arr[i]>max) max = arr[i];
    }
    int max_digit = 0;
    while(max !=0){
        max /=10;
        max_digit++;
    }

    int digit = 1;
    int r = 0; 
    for(int i=0; i<max_digit; i++){
        // 0~9 까지 돌면서 차곡차곡
        for(int j=0; j<10; j++){
            for(int k=0; k<N; k++){
                if((arr[k]/digit)%10 == j){
                    sorted[r] = arr[k];
                    r++;
                }
            }
        }
        for(int k=0; k<N; k++){
            arr[k] = sorted[k];
        }
        r = 0;
        digit *=10;
    }
    

}


int main() {

    // random arr gen
    int* r_arr_1000 = get_random_arr(1000);
    int* r_arr_5000 = get_random_arr(5000);
    int* r_arr_10000 = get_random_arr(10000);

    // worst arr gen
    int* w_arr_1000 = get_worst_arr(1000);
    int* w_arr_5000 = get_worst_arr(5000);
    int* w_arr_10000 = get_worst_arr(10000);


    // sort algorithm

    // bubble sort
    int r_bubble_1000[1000];    copy_arr(r_arr_1000, r_bubble_1000, 1000);
    int r_bubble_5000[5000];    copy_arr(r_arr_5000, r_bubble_5000, 5000);
    int r_bubble_10000[10000];  copy_arr(r_arr_10000, r_bubble_10000, 10000);
    int w_bubble_1000[1000];    copy_arr(w_arr_1000, w_bubble_1000, 1000);
    int w_bubble_5000[5000];    copy_arr(w_arr_5000, w_bubble_5000, 5000);
    int w_bubble_10000[10000];  copy_arr(w_arr_10000, w_bubble_10000, 10000);

        // bubble_sort(r_bubble_1000, 1000);
        // compare_arr(r_arr_1000, r_bubble_1000, 1000);

        // bubble_sort(w_bubble_1000, 1000);
        // compare_arr(w_arr_1000, w_bubble_1000, 1000);


    // insert sort
    int r_insert_1000[1000];    copy_arr(r_arr_1000, r_insert_1000, 1000);
    int r_insert_5000[5000];    copy_arr(r_arr_5000, r_insert_5000, 5000);
    int r_insert_10000[10000];  copy_arr(r_arr_10000, r_insert_10000, 10000);
    int w_insert_1000[1000];    copy_arr(w_arr_1000, w_insert_1000, 1000);
    int w_insert_5000[5000];    copy_arr(w_arr_5000, w_insert_5000, 5000);
    int w_insert_10000[10000];  copy_arr(w_arr_10000, w_insert_10000, 10000);

        // insert_sort(r_insert_1000, 1000);
        // compare_arr(r_arr_1000, r_insert_1000, 1000);


    // merge sort
    int r_merge_1000[1000];    copy_arr(r_arr_1000, r_merge_1000, 1000);
    int r_merge_5000[5000];    copy_arr(r_arr_5000, r_merge_5000, 5000);
    int r_merge_10000[10000];  copy_arr(r_arr_10000, r_merge_10000, 10000);
    int w_merge_1000[1000];    copy_arr(w_arr_1000, w_merge_1000, 1000);
    int w_merge_5000[5000];    copy_arr(w_arr_5000, w_merge_5000, 5000);
    int w_merge_10000[10000];  copy_arr(w_arr_10000, w_merge_10000, 10000);

        // int merge_sorted[1000];
        // merge_sort(r_merge_1000, merge_sorted, 0, 999);
        // compare_arr(r_arr_1000, merge_sorted, 1000);


    // Radix sort
    int r_radix_1000[1000];    copy_arr(r_arr_1000, r_radix_1000, 1000);
    int r_radix_5000[5000];    copy_arr(r_arr_5000, r_radix_5000, 5000);
    int r_radix_10000[10000];  copy_arr(r_arr_10000, r_radix_10000, 10000);
    int w_radix_1000[1000];    copy_arr(w_arr_1000, w_radix_1000, 1000);
    int w_radix_5000[5000];    copy_arr(w_arr_5000, w_radix_5000, 5000);
    int w_radix_10000[10000];  copy_arr(w_arr_10000, w_radix_10000, 10000);    

    radix_sort(r_radix_1000, 1000);
    compare_arr(r_arr_1000, r_radix_1000, 1000);


}