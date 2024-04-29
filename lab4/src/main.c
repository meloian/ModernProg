#include <stdio.h>
#include "../include/account.h"

int main() {
    printf("Initial heap usage: %zu bytes\n", get_current_heap_usage());
    createAndDisplayAccountOnStack();  // work with stack memory
    printf("Heap usage after stack operation: %zu bytes\n", get_current_heap_usage());
    createAndDisplayAccountOnHeap();   // work with heap memory
    printf("Final heap usage: %zu bytes\n", get_current_heap_usage());
    return 0;
} 
