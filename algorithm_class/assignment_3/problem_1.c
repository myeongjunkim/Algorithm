
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

Node get_node(LinkedList* L, int index){
    
    Node* pre_node = (*L).head;
    for(int i=0; i<index; i++){
        pre_node = pre_node->next;
        // printf("%d\n",pre_node->data);
    }
    Node index_node = *(pre_node->next);
    return index_node;
}

void append_node(LinkedList* L, int n){
    Node* new_node = malloc(sizeof(Node));
    new_node->data = n;
    new_node->next = NULL;
    
    Node* pos_node = (*L).head;
    while(pos_node->next != NULL){
        pos_node = pos_node->next;
    }
    pos_node->next = new_node;
    L->size++;
}

void insert_node(LinkedList* L, int index, int n){
    if (L->size < index){
        printf("index out of range\n");
    } else{
        Node* new_node = malloc(sizeof(Node));
        new_node->data = n;
        new_node->next = NULL;

        Node* pre_node = (*L).head;
        for(int i=0; i<index; i++){
            pre_node = pre_node->next;
        }
        new_node->next = pre_node->next;
        pre_node->next = new_node;
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
        pre_node->next = temp->next;
        // free(temp); 
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

void traverse_list(LinkedList* L){
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
        append_node(&linked_list, rand()%10);
    }

    printf("\n[Generate a linked list of size 10 whose elements are chosen randomly]\n");
    traverse_list(&linked_list);

    printf("\nappend_node(&linked_list, 99999)\n");
    append_node(&linked_list, 99999);
    traverse_list(&linked_list);


    printf("\ninsert_node(&linked_list, 2, 10000)\n");
    insert_node(&linked_list, 2, 1000);
    traverse_list(&linked_list);

    printf("\nremove_node(&linked_list, 2)\n");
    remove_node(&linked_list, 2);
    traverse_list(&linked_list);

    printf("\nreverse_list(&linked_list)\n");
    reverse_list(&linked_list);
    traverse_list(&linked_list);

    printf("\n");

}

