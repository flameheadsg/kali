#include <stdio.h>

// declare the prototype of get_max
int get_max(int *arr, int n);

// declare the prototype of get_min
int get_min(int *arr, int n);

// Now implement the function get_max
int get_max(int *arr, int n) {
    int i = 0;
    int max = *arr;
    for (i = 0; i < n; i++) {
        if (*(arr + i) > max) max = *(arr + i);
    }
    
    return max;
}

// Now implement the function get_min
int get_min(int *arr, int n) {
    int i = 0;
    int min = *arr;
    for (i = 0; i < n; i++) {
        if (*(arr + i) < min) min = *(arr + i);
    }
    
    return min;
}

void get_max_min_sum(int *arr, int n, int *p_sum) {
    
    // call get_max to get the maximum in the array arr, you will need to pass the base address arr and n to this function.
    int max = get_max(arr, n);
    
    // Call get_min in the similar way and get the minimum value in the array, here also you will need to pass 2 parameters, base address of the array and the number of elements in that array.
    int min = get_min(arr, n);
    
    // find the sum of the maximum and minimum and then assign the sum to the integer pointed by p_sum.
    int sum = max + min;
    *p_sum = sum;
    return;
}

int main() {
	int arr[9] = { 10, 20, 30, 40, 50, 60, 70, 80, 90 };
	printf("Testing max_min_sum with values:\n{ 10, 20, 30, 40, 50, 60, 70, 80, 90 }\n");

	int sum = 0;
	int *p_sum = &sum;
	get_max_min_sum(arr, 9, p_sum);

	printf("Sum of array's max and min values is: %d\n", *p_sum);
	return 0;
}
