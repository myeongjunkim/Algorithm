#include<stdio.h>


int main() {
    int matrix[5][5] = {
        {1,1,1,1,1},
        {2,2,2,2,2},
        {3,3,3,3,3},
        {4,4,4,4,4},
        {5,5,5,5,5}
    };

    int rotated_matrix[5][5];
    for(int i=0; i <5; i++){
        for(int j=0; j<5; j++){
            rotated_matrix[j][4-i] = matrix[i][j];            
        }
    }

    for(int i=0; i <5; i++){
        for(int j=0; j<5; j++){
            printf("%d ",rotated_matrix[i][j]);
        }
        printf("\n");
    }

}