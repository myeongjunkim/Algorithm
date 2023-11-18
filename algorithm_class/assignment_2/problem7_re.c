#include<stdio.h>
#include <stdlib.h>
#include <time.h>

int (* get_matrix1())[10]{
    srand(time(NULL));
    static int matrix1[30][10];
	for (int i = 0; i< 30; i++) {
        for (int j=0; j<10; j++) {
            matrix1[i][j] = rand()%9+1;
        }
	}
    return matrix1;
}


int (* get_matrix2())[50]{
    srand(time(NULL));
    static int matrix2[10][50];
	for (int i = 0; i< 10; i++) {
        for (int j=0; j<50; j++) {
            matrix2[i][j] = rand()%9+1;
        }
	}
    return matrix2;
}


int (* multify_matrix(int (*matrix1)[10], int (*matrix2)[50]))[50]{
    
    static int result[30][50];
    for(int i = 0; i < 30; i++) {
		for(int j = 0; j < 50; j++){
		    result[i][j] = 0;
			for(int k = 0; k < 10; k++)	{
				result[i][j] += matrix1[i][k] * matrix2[k][j]; 
            }
		}
    }
    return result;
}

int main(){

    int (*matrix1)[10];
    matrix1 = get_matrix1();
    int (*matrix2)[50];
    matrix2 = get_matrix2();
    
    int (*matrix_case1)[50];
    matrix_case1 = multify_matrix(matrix1, matrix2);

    for(int i=0; i<30; i++){
        for(int j=0; j<50; j++){
            printf("%d ", matrix_case1[i][j]);
        }
        printf("\n");
    }
    
    

}