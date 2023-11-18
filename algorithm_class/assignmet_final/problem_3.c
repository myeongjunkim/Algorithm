#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_SIZE 5

typedef struct {
    int pre_node;
} Node;

Node node_case[MAX_SIZE];
int distance[MAX_SIZE];

int get_min_index(int distance[], int visited[]){
    int min = INT_MAX;
    int min_index;
    for(int i=0; i<MAX_SIZE; i++){
        if ( visited[i] == 0 && (min>distance[i])){
            min = distance[i];
            min_index = i;
        } 
    }
    return min_index;
}

// 다익스트라 로직
void dijkstra(int gragh[][MAX_SIZE], int n_source){
    
    // 빽트랙킹용 노드 초기화
    for(int i=0; i<MAX_SIZE; i++){
        node_case[i].pre_node = -1;
    }

    // source 로부터 각 거리 그래프에서 초기화,  distance를 바꿔가며 진행
    int visited[MAX_SIZE];
    for(int i=0; i<MAX_SIZE; i++){
        distance[i] = gragh[n_source][i];
        visited[i] = 0;
        if (distance[i] != INT_MAX && distance[i] !=0) node_case[i].pre_node = n_source;
    }

    visited[n_source] = 1;

    int pos;
    for(int i=0; i<MAX_SIZE-1; i++){
        // 방문이 찍히니까 pos도 계속 바뀐다.
        pos = get_min_index(distance, visited);
        for (int v=0; v<MAX_SIZE; v++){
            if (visited[v] == 0 && distance[pos] != INT_MAX && gragh[pos][v] != INT_MAX && distance[v]>distance[pos]+gragh[pos][v]){
                distance[v] = distance[pos] + gragh[pos][v];
                node_case[v].pre_node = pos;


            }
        }
        visited[pos] = 1;
    }
}

int main() {

    char c_node[] = {'s', 't', 'x', 'y', 'z'};

    int gragh[][MAX_SIZE]={
       //s t x y z
        {0,3,INT_MAX,5,INT_MAX}, // s ->0
        {INT_MAX,0,6,2,INT_MAX}, // t ->1
        {INT_MAX,INT_MAX,0,INT_MAX,2}, // x ->2
        {INT_MAX,1,4,0,6}, // y ->3
        {3,INT_MAX,7,INT_MAX,0}, // z ->4        
    };
    
    dijkstra(gragh, 0);

    // for(int i=0; i<MAX_SIZE; i++){
    //     printf("source -> %c : %d\n", c_node[i], distance[i]);
    // }

    int z = 4; // z
    int z_route[MAX_SIZE];

    int z_size=0;
    while(1){
        z_route[z_size++] = z;
        z = node_case[z].pre_node;
        if (z == -1) break;
    }

    int y = 3; // z
    int y_route[MAX_SIZE];

    int y_size=0;
    while(1){
        y_route[y_size++] = y;
        y = node_case[y].pre_node;
        if (y == -1) break;
    }

    printf("y route : ");
    for(int i=y_size-1; i>=0; i--) printf("%c ", c_node[y_route[i]]);
    printf(" // [s - y] costs : %d", distance[3]);
    printf("\n");

    printf("z route : ");
    for(int i=z_size-1; i>=0; i--) printf("%c ", c_node[z_route[i]]);
    printf(" // [s - z] costs : %d", distance[4]);
    printf("\n");

}