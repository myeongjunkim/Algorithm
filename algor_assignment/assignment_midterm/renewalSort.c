#include <stdio.h>
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
    printf("배열 출력\n\n");
    for(int i=0; i<N; i++){
        printf("%d번째 : %d\n", i, arr[i]);
    }
}

void compare_arr(int* arr, int* arr2, int N){
    printf("\nprint before and after\n\n");
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

void merge_sort(int* arr, int left, int right){
    int mid = (left+right)/2;
    if(left<right){
        merge_sort(arr, left, mid);
        merge_sort(arr, mid+1, right);
    }
    int *sorted = (int*) malloc (sizeof(int) * (right-left+1));
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
    while(i<=mid) sorted[k++] = arr[i++];
    while(j<=right) sorted[k++] = arr[j++];

    for(int i=left; i<=right; i++) arr[i] = sorted[i];

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

    // 자릿수만큼 돌면서 sorted 배열애 각 자릿수 기준으로 정렬 
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

int partition(int* arr, int l, int r){
    int x = arr[l];
    int i = l;
    int temp;
    for(int j=l+1; j<=r; j++){
        if(arr[j]<x){
            i++;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    temp = arr[l];
    arr[l] = arr[i];
    arr[i] = temp;
    return i;
}

void quick_sort(int* arr, int l, int r){
    if(l<r){
        int mid = partition(arr, l, r);
        quick_sort(arr, l, mid-1);
        quick_sort(arr, mid+1, r);
    }
}

void bucket_sort(int* arr, int N){
    int size;
    if (N<=1000) size = 50;
    else if (N<=5000) size = 250;
    else size = 500;
    int** bucket = (int**)malloc(sizeof(int*) * size);
    for(int i=0; i<size; i++){
        bucket[i] = (int*) malloc (sizeof(int) * N);
    }

    // 구간별 평균 개수
    int num = ceil(N/size);
    int* bucket_top = malloc(sizeof(int) * size);
    int b_index, top;
    for(int i=0; i<N; i++){
        b_index = floor(arr[i]/num);
        top = bucket_top[b_index]; // top 관리(Bucket에 들어있는 총 개수)
        bucket[b_index][top] = arr[i];
        bucket_top[b_index]++;
    }

    int total_index=0;
    for(int i=0; i<size; i++){
        insert_sort(bucket[i], bucket_top[i]);
        for(int j=0; j<bucket_top[i]; j++){
            arr[total_index+j] = bucket[i][j];
        }
        total_index += bucket_top[i];
    }
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main() {

    // 정렬이 필요한 origin arr 생성 
    int N[3] = {1000, 5000, 10000};
    int* test_arr_origin[6];
    for(int i=0; i<6; i++){
        // 앞에 세개는 random 배열 1000, 5000, 10000
        if (i<3) test_arr_origin[i] = get_random_arr(N[i%3]);
        // 뒤에 세개는 worst 배열 1000, 5000, 10000
        else test_arr_origin[i] = get_worst_arr(N[i%3]);
    }

    // sort algorithm
    clock_t start;
    clock_t end;


    // bubble sort

    // bubble 테스트용 원본 복사
    int** bubble_sorted_arr_list = (int**)malloc(sizeof(int*) * 6);
    for(int i=0; i<6; i++){
        bubble_sorted_arr_list[i] = (int*) malloc (sizeof(int) * N[i%3]);
        copy_arr(test_arr_origin[i], bubble_sorted_arr_list[i], N[i%3]);
    }

    double bubble_result[6];
    for(int i=0; i<6; i++){
        start = clock();
        bubble_sort(bubble_sorted_arr_list[i], N[i%3]);
        end = clock();
        bubble_result[i] = (double)(end-start)/CLOCKS_PER_SEC;
    }
    // compare_arr(test_arr_origin[0], bubble_sorted_arr_list[0], 1000);


    // insert sort
    int** insert_sorted_arr_list = (int**)malloc(sizeof(int*) * 6);
    for(int i=0; i<6; i++){
        insert_sorted_arr_list[i] = (int*) malloc (sizeof(int) * N[i%3]);
        copy_arr(test_arr_origin[i], insert_sorted_arr_list[i], N[i%3]);
    }

    double insert_result[6];
    for(int i=0; i<6; i++){
        start = clock();
        insert_sort(insert_sorted_arr_list[i], N[i%3]);
        end = clock();
        insert_result[i] = (double)(end-start)/CLOCKS_PER_SEC;
    }



    // merge sort
    int** merge_sorted_arr_list = (int**)malloc(sizeof(int*) * 6);
    for(int i=0; i<6; i++){
        merge_sorted_arr_list[i] = (int*) malloc (sizeof(int) * N[i%3]);
        copy_arr(test_arr_origin[i], merge_sorted_arr_list[i], N[i%3]);
    }

    double merge_result[6];
    for(int i=0; i<6; i++){
        start = clock();
        merge_sort(merge_sorted_arr_list[i],0, N[i%3]-1);
        end = clock();
        merge_result[i] = (double)(end-start)/CLOCKS_PER_SEC;
    }
    // compare_arr(test_arr_origin[0], merge_sorted_arr_list[0], 1000);


    // Radix sort
    int** radix_sorted_arr_list = (int**)malloc(sizeof(int*) * 6);
    for(int i=0; i<6; i++){
        radix_sorted_arr_list[i] = (int*) malloc (sizeof(int) * N[i%3]);
        copy_arr(test_arr_origin[i], radix_sorted_arr_list[i], N[i%3]);
    }

    double radix_result[6];
    for(int i=0; i<6; i++){
        start = clock();
        radix_sort(radix_sorted_arr_list[i], N[i%3]);
        end = clock();
        radix_result[i] = (double)(end-start)/CLOCKS_PER_SEC;
    }
    // compare_arr(test_arr_origin[0], radix_sorted_arr_list[0], 1000);


    // Quick sort
    int** quick_sorted_arr_list = (int**)malloc(sizeof(int*) * 6);
    for(int i=0; i<6; i++){
        quick_sorted_arr_list[i] = (int*) malloc (sizeof(int) * N[i%3]);
        copy_arr(test_arr_origin[i], quick_sorted_arr_list[i], N[i%3]);
    }

    double quick_result[6];
    for(int i=0; i<6; i++){
        start = clock();
        quick_sort(quick_sorted_arr_list[i],0, N[i%3]-1);
        end = clock();
        quick_result[i] = (double)(end-start)/CLOCKS_PER_SEC;
    } 
    // compare_arr(test_arr_origin[0], quick_sorted_arr_list[0], 1000);



    // Bucket sort
    int** bucket_sorted_arr_list = (int**)malloc(sizeof(int*) * 6);
    for(int i=0; i<6; i++){
        bucket_sorted_arr_list[i] = (int*) malloc (sizeof(int) * N[i%3]);
        copy_arr(test_arr_origin[i], bucket_sorted_arr_list[i], N[i%3]);
    }

    double bucket_result[6];
    for(int i=0; i<6; i++){
        start = clock();
        bucket_sort(bucket_sorted_arr_list[i], N[i%3]);
        end = clock();
        bucket_result[i] = (double)(end-start)/CLOCKS_PER_SEC;
    } 
    // compare_arr(test_arr_origin[0], bucket_sorted_arr_list[0], 1000);

    printf("\n<Total algorithm speed>\n");

    for(int i=0; i<6; i++){
        printf("\n[case%d]\n\n",i);
        printf("bubble : %f\n", bubble_result[i]);
        printf("insert : %f\n", insert_result[i]);
        printf("merge : %f\n", merge_result[i]);
        printf("radix : %f\n", radix_result[i]);
        printf("quick : %f\n", quick_result[i]);
        printf("bucket : %f\n", bucket_result[i]);
    }

}