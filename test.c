#include <stdio.h>

void print_binary(int n) { 
    int c, k; 
    for (c = 31; c >= 0; c--) {
    	k = n >> c;
 
    	if (k & 1)
    	    printf("1");
    	else
      	    printf("0");
    }
 
    printf("\n");
}

int main() {
	int a, b;
	void (*p)(int);
	p = print_binary;	

	printf("Practicing bit-wise arithmetic using function pointers!\n\n");
	printf("Enter the first integer operand a:\n");
	scanf("%i", &a);
	printf("Enter the second integer operand b:\n");
	scanf("%i", &b);

	printf("\nOperand a %d in binary:\n", a);
	p(a);
	printf("Operand b %d in binary:\n", b);
	p(b);

	printf("\na AND b:\n");
	p((int) (a & b));
	printf("a OR b:\n");
	p((int) (a | b));
	printf("a XOR b:\n");
	p((int) (a ^ b));

	printf("\na's LEFT SHIFT by 1:\n");
	p((int) (a << 1));
	printf("b's LEFT SHIFT by 1:\n");
	p((int) (b << 1));

	printf("\na's RIGHT SHIFT by 1:\n");
	p((int) (a >> 1));
	printf("b's RIGHT SHIFT by 1:\n");
	p((int) (b >> 1));

	printf("\na's COMPLEMENT:\n");
	p((int) (~a));
	printf("b's COMPLEMENT:\n");
	p((int) (~b));

        return 0;
}
