#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int arr[][3], int N){
    for(int i=0; i<N; i++){
        for(int j=N-1; j>i; j--){
            if((arr[j][2] / arr[j][1]) > (arr[j-1][2] / arr[j-1][1])){
                int temp[] = {arr[j][0], arr[j][1], arr[j][2]};
                arr[j][0] = arr[j-1][0];
                arr[j][1] = arr[j-1][1];
                arr[j][2] = arr[j-1][2];
                
                arr[j-1][0] = temp[0];
                arr[j-1][1] = temp[1];
                arr[j-1][2] = temp[2];
            }
        }
    }
}

int main(){
    int N=6; int max_weight = 16;
    int weight_value[][3] = {
        {1, 6, 60},
        {2, 10, 20},
        {3, 3, 12},
        {4, 5, 80},
        {5, 1, 30},
        {6, 3, 60}
    };
    printf("\n<before sorting>\n\n");
    for(int i=0; i<N; i++){
        printf("item : %d, weight : %d, value : %d\n", weight_value[i][0], weight_value[i][1], weight_value[i][2]);
    }
    bubble_sort(weight_value, 6);

    printf("\n<after sorting>\n\n");
    for(int i=0; i<N; i++){
        printf("item : %d, weight : %d, value : %d\n", weight_value[i][0], weight_value[i][1], weight_value[i][2]);
    }


    printf("\n<fractional knapsack>\n\n");
    // greedy algorithm
    int weight=0; int value = 0;
    for(int i=0; i<N; i++){
        if(weight + weight_value[i][1] <= max_weight){
            value += weight_value[i][2];
            weight += weight_value[i][1];
            printf("item %d (fraction_num : 1) -> ", weight_value[i][0]);
        } else {
            value +=  (max_weight - weight) * (weight_value[i][2] / weight_value[i][1]);
            printf("item %d (fraction_num : %d/%d)", weight_value[i][0], (max_weight-weight), weight_value[i][1]);
            printf("\n");
            break;
        }
    }

    printf("max_value : %d\n\n", value);

}