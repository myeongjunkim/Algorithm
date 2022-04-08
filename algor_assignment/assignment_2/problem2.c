#include<stdio.h>

int main() {
    char s1[100];
    printf("단어를 입력하세요: ");
    scanf("%s", s1);

    int length = 0;
    for (int i= 0; s1[i] != '\0'; i++){
        length++;
    }

    int N = length/2;
    int flag = 1;
    for(int i= 0; i<N; i++){
        if(s1[i] != s1[length-1-i]){
            flag = 0;
            break;
        }
    }

    if (flag){
        printf("%s is palindrom\n", s1);
    } else{
        printf("%s is not palindrom\n", s1);
    }

    return 0;

}