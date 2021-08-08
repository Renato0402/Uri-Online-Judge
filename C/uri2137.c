#include <stdio.h>
#include <stdlib.h>



int comp(const void * n1,const void* n2){

if(*(int*)n1 > *(int*)n2)return 1;
if(*(int*)n1 < *(int*)n2)return -1;
return 0;

}


int main(){

int n;
int ns;
int v[1000];
int aux = 0;

while(scanf("%d",&n)!= EOF){
 int cont = n;

 while(n--){
    scanf("%d",&ns);
    v[aux++] = ns;


 }

 qsort(v,cont,sizeof(int),comp);

 for(int i = 0; i < cont;i++){

    int a = v[i];
    int cont = 0;

    while(a!=0){
        cont++;
        a = a/10;
    }

    int aux = 4-cont;
    if(v[i] == 0)aux=3;
     while(aux--){
       printf("0");
    }

    printf("%d\n",v[i]);

 }
   aux = 0;


}

return 0;

}

