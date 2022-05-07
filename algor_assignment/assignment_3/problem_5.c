#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    char color;
    struct Node* left;
    struct Node* right;
} Node;

typedef struct Tree {
    Node* head;
} Tree;

void inorder(Node* node){
    if(node !=NULL){
        inorder(node->left);
        printf("%d ", node->data);
        inorder(node->right);
    }
}

void preorder(Node* node){
    if(node !=NULL){
        printf("%d ", node->data);
        inorder(node->left);
        inorder(node->right);
    }
}

void postorder(Node* node){
    if(node !=NULL){
        inorder(node->left);
        inorder(node->right);
        printf("%d ", node->data);
    }
}

void r_rotation(Tree* T, Node node);
void l_rotation(Tree* T, Node node);

void insert_node(Tree* T, Node* node){

    Node* pre_node = T->head;
    Node* pos_node = T->head;
    while(1){
        // 왼쪽
        if(node->data < pos_node->data){
            if(pos_node->left == NULL){
                pos_node->left = node;
                // 문제 시작
                if(pos_node->color == 'r'){
                    
                    if(pre_node->left == pos_node){
                        // LL인 상황
                        if(pre_node->right == NULL || pre_node->right->color == 'b'){
                            // 회전!!
                            printf("");
                        } else{
                            // 색변환
                            pos_node->color = 'b';
                            pre_node->right->color = 'b';
                            if(pre_node != T->head) pre_node->color= 'r';
                        }
                    } else {
                        // RL인 상황
                        if(pre_node->left == NULL || pre_node->left->color == 'b'){
                            // 회전!!
                            printf("");
                        } else{
                            pos_node->color = 'b';
                            pre_node->left->color = 'b';
                            if(pre_node != T->head) pre_node->color= 'r';
                        }

                    }
                    
                }
                break;
            }
            else{
                pre_node = pos_node;
                pos_node = pos_node->left;
            }
        // 오른쪽
        } else {
            if(pos_node->right == NULL){
                pos_node->right = node;

                // 문제 시작
                if(pos_node->color == 'r'){
                    
                    if(pre_node->left == pos_node){
                        // LR인 상황
                        if(pre_node->right == NULL || pre_node->right->color == 'b'){
                            // 회전!!
                            printf("");
                        } else{
                            // 색변환
                            pos_node->color = 'b';
                            pre_node->right->color = 'b';
                            if(pre_node != T->head) pre_node->color= 'r';
                        }
                    } else {
                        // RR인 상황
                        if(pre_node->left == NULL || pre_node->left->color == 'b'){
                            // 회전!!
                            printf("");
                        } else{
                            pos_node->color = 'b';
                            pre_node->left->color = 'b';
                            if(pre_node != T->head) pre_node->color= 'r';
                        }

                    }
                    
                }

                break;
            } 
            else{
                pre_node = pos_node;
                pos_node = pos_node->right;
            } 
        }
        
    }   
}

void make_rbTree(Tree* T, int arr[], int N){
    
    Node* head_node = malloc(sizeof(Node));
    head_node->data = arr[0];
    head_node->color = 'b';
    T->head = head_node;

    for(int i=1; i<N; i++){
        Node* new_node = malloc(sizeof(Node));
        new_node->data = arr[i];
        new_node->color = 'r';

        insert_node(T, new_node);
    }
}

int main(){
    
    Tree* T = malloc(sizeof(Tree));
    int arr[] = {41, 38, 31, 12, 19, 8};
    int N = sizeof(arr)/sizeof(int);

    make_rbTree(T, arr, N);

    inorder(T->head);
    
    
}