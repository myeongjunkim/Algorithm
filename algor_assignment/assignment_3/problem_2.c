
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

void delete_duplicates(LinkedList* L){
    Node* pos_node = (*L).head->next;
    Node* check_node = malloc(sizeof(Node));

    int i=0;
    while(pos_node->next != NULL){
        check_node = pos_node->next;
        int j = i+1;
        while(check_node !=NULL){
            if(pos_node->data == check_node->data){
                printf("%d is duplicated\n", pos_node->data);
                remove_node(L, j--);
            }
            check_node = check_node->next;
            j++;
        }
        pos_node = pos_node->next;
        i++;
    }
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

    for(int i=0; i<20; i++){
        append_node(&linked_list, rand()% 51);
    }

    printf("\n[Generate a linked list of size 20 whose elements are from 1 to 50]\n\n");
    traverse_list(&linked_list);
    printf("\n");

    delete_duplicates(&linked_list);
    printf("\n");

    traverse_list(&linked_list);

    printf("\n");
}