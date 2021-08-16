#include <stdio.h>
#include <stdlib.h>


int main(){

int cases;
char palavra[1100];
unsigned short half;
unsigned short size;

scanf("%d",&cases);

while(cases--){

 scanf(" %[^\n]",palavra);

 size = strlen(palavra);
 half = size/2;


 for(int i = 0 ; i < size;i++){

    if((palavra[i]>='A' && palavra[i] <='Z') ||(palavra[i]>='a' && palavra[i] <='z'))
        palavra[i]+=3;

 }

 for(int i = 0 ; i < half;i++){

    char aux = palavra[i];
    palavra[i] = palavra[--size];
    palavra[size] = aux;

 }

 for(int i = half ; i < strlen(palavra);i++){

    palavra[i]-=1;
 }

 printf("%s\n",palavra);

 memset(palavra,0,sizeof(palavra));

}
return 0;

}

