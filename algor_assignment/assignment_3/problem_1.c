#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct LinkedList {
    Node* head;
} LinkedList;

int get_node(LinkedList* L, int index){
    
    Node* pre_node = (*L).head;
    for(int i=0; i<index; i++){
        pre_node = pre_node->next;
        // printf("%d\n",pre_node->data);
    }
    Node index_node = *(pre_node->next);
    return index_node.data;
}

int main(){

    // srand(time(NULL));

    Node* head = malloc(sizeof(Node));
    
    LinkedList linked_list;
    linked_list.head = head;

    Node* pre_node = linked_list.head;
    for(int i=0; i<10; i++){
        Node* new_node = malloc(sizeof(Node));
        new_node->data = i;
        new_node->next = NULL;

        pre_node->next = new_node;
        pre_node = new_node;
    }

  
    printf("%d\n", get_node(&linked_list,9));

    // printf("%d", linked_list.head->next->next->next->data);



    



}

