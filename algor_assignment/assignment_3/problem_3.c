
#include <stdio.h>

int main(){

    int arr[] = {8, 3, 9, NULL, NULL, 4, 7};
    int N = sizeof(arr)/sizeof(int);
    
    int flag = 1;
    for(int i=0; i<N; i++){
        if(2*i+1<N && arr[2*i+1] != NULL){
            if(arr[i]<arr[2*i+1]){
                flag=0;
                break;
            } 
        }
        if(2*i+2<N && arr[2*i+2] != NULL){
            if(arr[i]>arr[2*i+2]){
                flag=0;
                break;
            }
        }
    }
    if(flag) printf("\nbinary search tree O\n\n");
    else printf("\nbinary search tree X\n\n");
}