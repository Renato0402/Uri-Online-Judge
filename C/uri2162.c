#include <stdio.h>
#include <stdlib.h>


int main()
{
   int size;

   scanf("%d",&size);

   int n[size];

   int in;

   int flagAux = 0;

   int flag = 0;

   for(int i = 0; i < size;i++){

    scanf("%d",&in);
    n[i] = in;
   }

   if(n[0] > n[1]) flagAux = 1;

   if(flagAux){

      for(int i = 0; i < size-1;i++){
        if(i%2==0){
            if(n[i] > n[i+1])flag = 1;
            else{
                flag = 0;
            }

        } else {
            if(n[i] < n[i+1])flag = 1;
            else{
                flag = 0;
            }
        }
     }

   } else {

     for(int i = 0; i < size-1;i++){
        if(i%2==0){
            if(n[i] < n[i+1])flag = 1;
            else{
                flag = 0;
            }

        } else {
            if(n[i] > n[i+1])flag = 1;
            else{
                flag = 0;
            }
        }
     }




   }

   printf("%d\n",flag);


   return 0;

}

