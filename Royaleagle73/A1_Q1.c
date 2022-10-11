#include <stdio.h>
void replace_cube(int a[],int n)
{
  int i,count=1;
  for(i=0;i<5;i++)
  {
    if(i+1==n)
    {
      a[i]=(a[i]*a[i]*a[i]);
      count=count+1;
      n=n*count;
    }
  }
}
int main()
{
    int a[5]={1,2,3,4,5},n=2,i;
    replace_cube(a,n);
    for(i=0;i<5;i++)
    {
      printf("%d\t",a[i]);
    }
    return 0;
}
