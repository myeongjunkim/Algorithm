#include<stdio.h>

int main() {
    int target = 120;
    int numlist[] = {12, 34, 37, 45, 57, 82, 99, 120, 134};
    int numlist_len = sizeof(numlist)/sizeof(int);

    int start = 0;
    int end = numlist_len-1;
    int mid = (start+end)/2;
    while(numlist[mid]!=target){
        if(numlist[mid]>target){
            end = mid;
        } else{
            start = mid;
        }
        mid = (start+end)/2;
    }
    printf("%d is placed in %d-th\n",target, mid+1);
}