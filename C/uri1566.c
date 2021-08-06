#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define max 231


int main()
{
   int c,size,n,aux;
   int cont = 0;
   int altura[max] = {0};

   scanf("%d",&c);


   while(c--){
    scanf("%d",&size);
    aux = size;


     while(size--){
        scanf("%d",&n),altura[n]++;

     }

     for(int i = 20; i < max;i++){

        while(altura[i]!= 0){

            if (cont < aux-1){

            printf("%d ",i),altura[i]--;
            cont++;

            }else{
             printf("%d",i),altura[i]--;
            }

        }

     }

     printf("\n");
     cont = 0;
     memset(altura,0,sizeof(altura));
   }

   return 0;

}

