#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp (const void * n1, const void * n2)
{
    int f = *((int*)n1);
    int s = *((int*)n2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}


int main(){

int n;
int number;
int i = 0;
int j = 0;


scanf("%d",&n);

int par[n];
int impar[n];


while(n--){

    scanf("%d",&number);

    if(number%2 == 0){

       par[i] = number;
       i++;

    } else {

       impar[j] = number;
       j++;

    }


}


    qsort(par,i,sizeof(int),comp);
    qsort(impar,j,sizeof(int),comp);

    for(int k = 0; k < i;k++){
        printf("%d\n",par[k]);
    }

    for(int k = j-1; k >=0;k--){
        printf("%d\n",impar[k]);
    }




return 0;

}

