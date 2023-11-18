
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
        printf("[%d, %c] ", node->data, node->color);
        inorder(node->right);
    }
}

void preorder(Node* node){
    if(node !=NULL){
        printf("[%d, %c] ", node->data, node->color);
        preorder(node->left);
        preorder(node->right);
    }
}

void postorder(Node* node){
    if(node !=NULL){
        postorder(node->left);
        postorder(node->right);
        printf("[%d, %c] ", node->data, node->color);
    }
}

Node* search_pre_node(Tree* T, Node* node){
     
    Node* pos_node = T->head->left;

    if (T->head->left == node) return T->head; 

     while(1){
        if(node->data < pos_node->data){
            if(pos_node->left == node){
                return pos_node;
            } else {
                pos_node = pos_node->left;
            }
        } else {
            if(pos_node->right == node){
                return pos_node;
            } else {
                pos_node = pos_node->right;
            }
        }
     }
}

void r_rotation(Tree* T, Node* node){
    
    Node* center_node = node->left;
    node->left = center_node->right;
    center_node->right = node;
    center_node->color = 'b';
    node->color = 'r';

    Node* pre_node = search_pre_node(T, node);
    if (pre_node == T->head) T->head->left = center_node;
    else if (pre_node->left == node) pre_node->left = center_node;
    else pre_node->right = center_node;

}
void l_rotation(Tree* T, Node* node){

    Node* center_node = node->right;
    node->right = center_node->left;
    center_node->left = node;
    center_node->color = 'b';
    node->color = 'r';

    Node* pre_node = search_pre_node(T, node);
    if (pre_node == T->head) T->head->left = center_node;
    else if (pre_node->left == node) pre_node->left = center_node;
    else pre_node->right = center_node;

}

void insert_node(Tree* T, Node* node){

    Node* pre_node = T->head;
    Node* pos_node = T->head->left;
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
                            r_rotation(T, pre_node);
                        } else{
                            // 색변환
                            pos_node->color = 'b';
                            pre_node->right->color = 'b';
                            if(pre_node != T->head->left) pre_node->color= 'r';
                        }
                    } else {
                        // RL인 상황
                        if(pre_node->left == NULL || pre_node->left->color == 'b'){
                            // 회전!!
                            r_rotation(T, pos_node);
                            l_rotation(T, pre_node);
                        } else{
                            // 색변환
                            pos_node->color = 'b';
                            pre_node->left->color = 'b';
                            if(pre_node != T->head->left) pre_node->color= 'r';
                        }
                    }
                }
                break;
            }
            else{
