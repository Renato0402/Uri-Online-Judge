#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
bool b;


struct node {

 int data;
 struct node* left;
 struct node* right;

};

struct node* newNode(int v){

struct node* no = (struct node*)malloc(sizeof(struct node));
no->data = v;
no->left = no->right = NULL;

return no;
}

struct node* insert(struct node* root,int data){

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

bool search(struct node* root,int data){

 if(root == NULL) return false;
 else if (root-> data == data) return true;
 else if(data <= root->data)return search(root->left,data);
 else return search(root->right,data);


}

struct node* findMax(struct node* root){

   if(root->right == NULL) return root;
   else return findMax(root->right);
}

struct node* erase(struct node* root,int data){

   if(root == NULL) return root;
   else if(data < root->data)root->left = erase(root->left,data);
   else if (data > root->data) root->right = erase(root->right,data);
   else {

    if(root->left == NULL && root->right == NULL){
        free(root);
        root = NULL;
        return root;

    }

    else if(root->left == NULL){
        struct node* tmp = root;
        root = root->right;
        free(tmp);
        return root;

    }

    else if(root->right == NULL){
        struct node* tmp = root;
        root = root->left;
        free(tmp);
        return root;

    }

    else {
        struct node* tmp = findMax(root->left);
        root->data = tmp->data;
        root->left = erase(root->left,tmp->data);

    }

   }

   return root;

};




void prefixa(struct node* root){
 if(root == NULL)return;
 if(b){
  printf("%d",root -> data);
  b = false;
 }else{
  printf(" %d",root -> data);
 }
 prefixa(root->left);
 prefixa(root->right);

}

void infixa(struct node* root){
 if(root == NULL) return;
 infixa(root->left);
  if(b){
  printf("%d",root -> data);
  b = false;
 }else{
  printf(" %d", root -> data);
 }
 infixa(root->right);

}

void posfixa(struct node* root){
 if(root == NULL) return;
 posfixa(root->left);
 posfixa(root->right);
 if(b){
  printf("%d",root -> data);
  b = false;
 }else{

  printf(" %d", root -> data);
 }

}



int main()
{

struct node* root = NULL;
char s[10];
int n;

while(scanf("%s",&s)!= EOF){

    if(s[0]== 'I' && s[1]!='N'){

       scanf("%d",&n);

       root = insert(root,n);

    }

    if(s[0]=='P' && s[1]!='O' && s[1]!='R'){

        scanf("%d",&n);

        if(!search(root,n))printf("%d nao existe\n",n);
        else printf("%d existe\n",n);


    }

    if(s[0] == 'R'){

      scanf("%d",&n);

      if(search(root,n))root = erase(root,n);


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

