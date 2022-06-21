#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_SIZE 5

// typedef struct {
//     int start;
//     int end;
//     int w;
// } Line;

typedef struct {
    int pre_node;
} Node;

Node node_case[MAX_SIZE];
int distance[MAX_SIZE];

int BellmanFord(int gragh[][MAX_SIZE], int n_source){

    // 거리데이터 초기화
    for(int i=0; i<MAX_SIZE; i++) distance[i] =INT_MAX;
    distance[n_source] = 0;

    // 빽트랙킹용 노드 초기화
    for(int i=0; i<MAX_SIZE; i++){
        node_case[i].pre_node = -1;
    }

    for(int v=0; v<MAX_SIZE-1; v++){
        
        // 모든 간선 조사
        for(int start=0; start<MAX_SIZE; start++){
            for(int end=0; end<MAX_SIZE; end++){
                // 간선이 있다면
                if (gragh[start][end] != 0 && gragh[start][end] != INT_MAX){
                    // 더 작은 경로 발견
                    if(distance[start] != INT_MAX && distance[start] + gragh[start][end] < distance[end]){
                        distance[end] = distance[start] + gragh[start][end];
                        node_case[end].pre_node = start;
                    }
                }
            }
        }
    }

    for(int start=0; start<MAX_SIZE; start++){
        for(int end=0; end<MAX_SIZE; end++){
            // 간선이 있다면
            if (gragh[start][end] != 0 && gragh[start][end] != INT_MAX){
                // 더 작은 경로 발견
                if(distance[start] != INT_MAX && distance[start] + gragh[start][end] < distance[end]){
                    return 0;
                }
            }
        }
    }

    return 1;


}


int main(){

    char c_node[] = {'s', 't', 'x', 'y', 'z'};

    int gragh[][MAX_SIZE]={
       //s t x y z
        {0,5,INT_MAX,6,INT_MAX}, // s ->0
        {INT_MAX,0,5,8,-4}, // t ->1
        {INT_MAX,-2,0,INT_MAX,INT_MAX}, // x ->2
        {INT_MAX,INT_MAX,-3,0,9}, // y ->3
        {2,INT_MAX,4,INT_MAX,0}, // z ->4        
    };

    // int gragh[][MAX_SIZE]={
    //    //s t x y z
    //     {0,6,INT_MAX,7,INT_MAX}, // s ->0
    //     {INT_MAX,0,5,8,-4}, // t ->1
    //     {INT_MAX,-2,0,INT_MAX,INT_MAX}, // x ->2
    //     {INT_MAX,INT_MAX,-3,0,9}, // y ->3
    //     {2,INT_MAX,7,INT_MAX,0}, // z ->4        
    // };

    if(BellmanFord(gragh, 0)) printf("result : <True>\n");
    else printf("result : <False>\n");

    for(int i=0; i<MAX_SIZE; i++){
        printf("[source -> %c] distance: %2d   pre_node: %c\n", c_node[i], distance[i], c_node[node_case[i].pre_node]);
    }


}