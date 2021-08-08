#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


int main(){


int n1;
int n2;
int en;

scanf("%d",&en);

while(en--){

scanf("%d %d",&n1,&n2);

for(int i = n1;i<=n2;i++){
    printf("%d",i);
}


for(int i = n2;i>=n1;i--){
   int tmp = i;

   while(tmp >=1){
     printf("%d",tmp%10);
     tmp=tmp/10;

   }


}

printf("\n");

}


return 0;

}

