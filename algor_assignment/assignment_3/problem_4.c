
#include <stdio.h>

int get_ancestor(int arr[],int N, int input1, int input2){
    int i=0;
    while(i<N){
        if(arr[i] > input1){
            if(arr[i] > input2) i = 2*i+1;
            else return arr[i];
        } else {
            if(arr[i] > input2) return arr[i];
            else i = 2*i+2;
        }
    }
    return 0;
}

int main(){
    int arr[] = {6, 2, 8, 1, 3, 7, 9};
    int N = sizeof(arr)/sizeof(int);

    int input1, input2;
    printf("\ndata1: ");
    scanf("%d", &input1);
    printf("data2: ");
    scanf("%d", &input2);

    printf("common ancestor : %d\n",get_ancestor(arr, N, input1, input2));
}