#include <stdio.h>
#include <stdlib.h>



int main()
{



char s[1000];
int t = 0;
int aux = 0;

while(scanf("%s",&s)!= EOF){


    for(int i = 0; i < strlen(s);i++){

        if(s[i]=='(') aux++;
        if(s[i] == ')' && aux==0)t=1;
        if(s[i] == ')' && aux!=0)aux--;

    }

    if(!aux && !t)printf("correct\n");
    else printf("incorrect\n");

    t = 0;
    aux = 0;


}




return 0;

}

