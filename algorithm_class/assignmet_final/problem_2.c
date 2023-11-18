#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_QUEUE_SIZE 8

typedef struct {
    int d_source;
    int pre_node;
    int visited;
} Node;

typedef struct {
    // Node data[MAX_QUEUE_SIZE];   // 노드 번호
    int list[MAX_QUEUE_SIZE];
    int rear, front;
    // rear은 마지막 인덱스
    // front는 처음 바로 왼쪽, 애초에 인덱스 1 부터 넣는다
} Deque;

int q_is_empty(Deque *q){
	return ( q->front == q->rear );
}

int q_is_full(Deque *q){
	return (( q->rear + 1) % MAX_QUEUE_SIZE == q->front);
}

void q_insert(Deque* q, int n_node){
    if (q_is_full(q))
		printf("큐 꽉참");
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->list[ q->rear ] = n_node;
}

int q_popleft(Deque *q){
	if (q_is_empty(q))
		printf("큐 공백");
	q->front =  (q->front + 1) % MAX_QUEUE_SIZE  ;
	return q->list[ q->front ];
}

void q_init(Deque* q){
	q->front = q->rear =  0;
}



// 메인 로직
void bfs(int gragh[][MAX_QUEUE_SIZE], Node node_case[], int n_source){
    Deque* q = (Deque*)malloc(sizeof(Deque));
    int pos;
    node_case[n_source].visited = 1;
    q_insert(q, n_source);
    while(!q_is_empty(q)){
        pos = q_popleft(q);
        // printf("pop : %d\n", pos);

        for(int i=0; i<MAX_QUEUE_SIZE; i++){
            if(gragh[pos][i] == 1 && node_case[i].visited == 0){
                // printf("pos : %d, i: %d\n", pos, i);
                node_case[i].visited = 1;
                node_case[i].d_source = node_case[pos].d_source + 1;
                node_case[i].pre_node = pos;
                q_insert(q, i);
            }
        }
    }
}



int main(){

    char c_node[] = {'r', 's', 't', 'u', 'v', 'w', 'x', 'y'};
    int gragh[][MAX_QUEUE_SIZE]={
       //r s t u v w x y
        {0,1,0,0,1,0,0,0}, // r ->0
        {1,0,0,0,0,1,0,0}, // s ->1
        {0,0,0,1,0,1,1,0}, // t ->2
        {0,0,1,0,0,0,1,1}, // u ->3
        {1,0,0,0,0,0,0,0}, // v ->4
        {0,1,1,0,0,0,1,0}, // w ->5
        {0,0,1,1,0,1,0,1}, // x ->6
        {0,0,0,1,0,0,1,0}, // y ->7
    };

    // 노드 초기화, 여기에 노드 최종 정보 저장
    Node node_case[MAX_QUEUE_SIZE];
    // Node* node_case = (Node*)malloc(sizeof(Node) * MAX_QUEUE_SIZE); 
    for(int i=0; i<MAX_QUEUE_SIZE; i++){
        node_case[i].pre_node = -1;
        node_case[i].visited = 0;
        node_case[i].d_source = 0;
    }

    // bfs 에 node_case[1](source) 인덱스인 1 넣어놓고 시작
    bfs(gragh, node_case, 1);

    for(int i=0; i<MAX_QUEUE_SIZE; i++){
        printf("node %c -> d_source : %d, pre_node : %c\n", c_node[i], node_case[i].d_source, c_node[node_case[i].pre_node]);
    }   

}