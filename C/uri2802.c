#include <stdio.h>
#include <stdlib.h>


int main()
{
   long long int n;

   long long int ans = 0;

   scanf("%lld",&n);

   ans = 1 + (n * (n-1)) / 2 + (n * (n-1) * (n-2) * (n-3)) / 24;

   printf("%lld\n",ans);

   return 0;

}

