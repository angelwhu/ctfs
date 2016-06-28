#include <stdio.h>
#include <stdlib.h>
void nono();
int main(int argc,char **argv){
 int i;
 if(argc!=2){nono();}
 i=atoi(argv[1]);
 if(i<0){nono();}
 i=i+5;
 if(i>4){nono();}
 if(i<5){printf("%d",i);}
 return 0;
}
void nono(){
  printf("%d",1);
  exit(1);
}
