#include <stdio.h>
#include <time.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct LinkedList {
    Node* head;
    int size;
} LinkedList;

Node traverse_node(LinkedList* L, int index){
    
    Node* pre_node = (*L).head;
    for(int i=0; i<index; i++){
        pre_node = pre_node->next;
        // printf("%d\n",pre_node->data);
    }
    Node index_node = *(pre_node->next);
    return index_node;
}

void append_node(LinkedList* L, Node* node){
    Node* pos_node = (*L).head;
    while(pos_node->next != NULL){
        pos_node = pos_node->next;
    }
    pos_node->next = node;
    L->size++;
}

void insert_node(LinkedList* L, int index, Node* node){
    if (L->size < index){
        printf("index out of range\n");
    } else{
        Node* pre_node = (*L).head;
        for(int i=0; i<index; i++){
            pre_node = pre_node->next;
        }
        node->next = pre_node->next;
        pre_node->next = node;
        L->size++;
    }
}

void remove_node(LinkedList* L, int index){
    if (L->size < index){
        printf("index out of range\n");
    } else{
        Node* pre_node = (*L).head;
        for(int i=0; i<index; i++){
            pre_node = pre_node->next;
        }
        Node* temp = pre_node->next;
        pre_node->next = pre_node->next->next;
        free(temp); 
        L->size--;
    }
}

void reverse_list(LinkedList* L){
    Node* pos_node = L->head->next; // 0번 인덱스 노드
    Node* temp = pos_node->next; // 바로 다음 인덱스 노드
    pos_node->next = NULL; // 0번 인덱스 next 값 NULL;
    Node* next_node = malloc(sizeof(Node));
    while(temp != NULL){
        next_node = temp; 
        temp = temp->next;
        next_node->next = pos_node;
        pos_node = next_node;
    }
    L->head->next = pos_node;
    free(temp);
}    

void print_list(LinkedList* L){
    Node* pos_node = L->head;
    while(pos_node->next != NULL){
        pos_node = pos_node->next;
        printf("%d ", pos_node->data);
    }
    printf("\n");
}


int main(){

    srand(time(NULL));

    Node* head = malloc(sizeof(Node));
    head->next = NULL;
    
    LinkedList linked_list;
    linked_list.head = head;

    for(int i=0; i<10; i++){
        Node* new_node = malloc(sizeof(Node));
        new_node->data = i;
        // rand()%10
        new_node->next = NULL;

        append_node(&linked_list, new_node);
    }


    Node* new_node = malloc(sizeof(Node));
    new_node->data = 12334;

    // insert_node(&linked_list,0, new_node);

    
    
    print_list(&linked_list);
    // printf("traverse : %d\n", traverse_node(&linked_list,9).data);
    // printf("%d\n", linked_list.size);

    reverse_list(&linked_list);

    printf("reversed\n");
    print_list(&linked_list);




    // remove_node(&linked_list, 4);
    // print_list(&linked_list);
    
    // printf("%d\n", linked_list.size);




    



}

