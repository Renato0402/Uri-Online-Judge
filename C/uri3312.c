#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define max 36000

void fat(int v[],int tam,int n){

 int transporte,aux;
 for(int i = 1; i <=n;i++){
      transporte = 0;
     for(int j = 0; j <tam;j++){

        aux = i*v[j]+transporte;
        v[j] = aux%10;
        transporte = aux/10;

     }
     while(transporte){

        v[tam] = transporte%10;
        transporte = transporte/10;
        tam++;
    }


 }


 printf("%d! = ",n);

 for(int i = tam-1; i>=0; i--){
    printf("%d",v[i]);
 }
 printf("\n");

}


int main()
{
    int count;
    int n;
    int aux;
    int resp[max],tamanho=1;
    resp[0] = 1;
    scanf("%d",&count);

    while(count--){
        scanf("%d",&n);
        aux = 0;

        if(n == 2 || n == 3){

            fat(resp,tamanho,n);
            memset(resp,0,max);
            resp[0]=1;
            continue;

        } else{

            if(n%2 == 0 || n%3 == 0){

                continue;

            } else {

              for(int i = 5; i <= sqrt(n);i+=2){

                if(n%i == 0){
                    aux++;

                }

                if(aux >= 1){

                    break;
                }

              }

              if(aux == 0 && n != 1){

                fat(resp,tamanho,n);
                memset(resp,0,max);
                resp[0]=1;

              }


            }

        }


    }



   return 0;

}

