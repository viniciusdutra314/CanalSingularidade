#include <stdio.h>
int main() {
    double num1 = 0.1;
    double num2 = 0.2;
    double num3=0.3;
    //0.30000000000000004441
    printf("0.1 + 0.2 = %.20f\n",num1+num2 );
    //0.29999999999999998890
    printf("0.3 = %.20f\n",num3 );
}