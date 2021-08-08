#include <stdio.h>
#include <stdlib.h>


int main(){

int n;
int n2;
char s[21];
char s2[21];
int i = 0;

scanf("%d",&n);

while(n--){

    scanf("%d",&n2);
    i = 0;

    scanf("%s",&s);
    n2--;



    while(n2--){

    scanf("%s",&s2);
     if(strcmp(s,s2) != 0)i = 1;


    }

    if(i)printf("ingles\n");
    else printf("%s\n",s);
}



return 0;

}

