#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
bool b;

struct node {

 char data;
 struct node* left;
 struct node* right;

};

struct node* newNode(char v){

struct node* no = (struct node*)malloc(sizeof(struct node));
no->data = v;
no->left = no->right = NULL;

return no;
}

struct node* insert(struct node* root,char data){

 if(root == NULL){

    root = newNode(data);
    return root;

 } else if(data <= root->data){
     root->left = insert(root->left,data);

 } else {

   root->right = insert(root->right,data);
 }

 return root;




};

bool search(struct node* root,char data){

 if(root == NULL) return false;
 else if (root-> data == data) return true;
 else if(data <= root->data)return search(root->left,data);
 else return search(root->right,data);


}

void prefixa(struct node* root){
 if(root == NULL)return;
 if(b){
  printf("%c", root -> data);
  b = false;
 }else{
  printf(" %c", root -> data);
 }
 prefixa(root->left);
 prefixa(root->right);

}

void infixa(struct node* root){
 if(root == NULL) return;
 infixa(root->left);
  if(b){
  printf("%c", root -> data);
  b = false;
 }else{
  printf(" %c", root -> data);
 }
 infixa(root->right);

}

void posfixa(struct node* root){
 if(root == NULL) return;
 posfixa(root->left);
 posfixa(root->right);
 if(b){
  printf("%c", root -> data);
  b = false;
 }else{
  printf(" %c", root -> data);
 }

}



int main()
{

struct node* root = NULL;
char s[10];

while(fgets(s,sizeof(s),stdin)!= EOF){

    if(s[0] == 'I' && strlen(s) < 5){

        root = insert(root,s[2]);


    }

    if(s[0] == 'P' && strlen(s) < 5){

        if(!search(root,s[2]))printf("%c nao existe\n",s[2]);
        else printf("%c existe\n",s[2]);

    }



    if(strstr(s,"INFIXA")!= NULL){

     b = true;
     infixa(root);
     printf("\n");


    }
    if(strstr(s,"PREFIXA")!= NULL){

     b = true;
     prefixa(root);
      printf("\n");

    }
    if(strstr(s,"POSFIXA")!= NULL){

      b = true;
      posfixa(root);
       printf("\n");

    }

}


return 0;

}

