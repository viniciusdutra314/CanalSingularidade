#include <math.h>
#include <stdio.h>

int main(){
    short int a=pow(2,15); //1 bit para o sinal (0=positivo 1=negativo)
    int b=pow(2,31);
    long int c=pow(2,63);
    printf("Short int: max=%d (3.2E4) e %d-bits \n",a,8*sizeof(a));
    printf("Int: max=%d (2.1E9) e %d-bits \n",b,8*sizeof(b));
    printf("Long Int: max=%ld (9.2E18) e %d-bits \n",c,8*sizeof(c));
    printf("----OverFlow---- \n");
    printf("Quando passamos do limite o valor faz um 'loop' no intervalo \n");
    a=a+1; b=b+1 ; c=c+1;
    printf("%d \n",a);
    printf("%d \n",b);
    printf("%ld \n",c);
   }