#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>  // verify heap boundaries with sbrk().
#include "../include/account.h"

static size_t current_heap_usage = 0;  // tracks the current heap usage
static void* last_heap_address = NULL;  // stores the last allocated heap address

void* custom_malloc(size_t size) {
    void* ptr = malloc(size);
    if (ptr) {
        current_heap_usage += size;
        last_heap_address = ptr;
    }
    return ptr;
}

void custom_free(void* ptr, size_t size) {
    if (ptr) {
        free(ptr);
        current_heap_usage -= size;
        if (ptr == last_heap_address) {
            last_heap_address = NULL;
        }
    }
}

// checks if the allocated memory address is within the heap boundaries 
void assert_heap_address(void *ptr) {
    void *heap_start = sbrk(0); // get the current end of the heap
    if (ptr != last_heap_address || ptr >= heap_start) {
        fprintf(stderr, "Heap address is invalid or not the last allocated address\n");
        exit(EXIT_FAILURE);
    }
}

// demonstrates creating and displaying an account object on the stack
void createAndDisplayAccountOnStack() {
    Account myAccount;  // stack allocation
    myAccount.id = 1;
    myAccount.balance = 1000.50;
    printf("Account on Stack - ID: %d, Balance: %.2f\n", myAccount.id, myAccount.balance);
    printf("Heap usage inside stack function: %zu bytes\n", get_current_heap_usage());
}

// demonstrates creating and displaying an account object on the heap
void createAndDisplayAccountOnHeap() {
    printf("Heap usage before allocation: %zu bytes\n", get_current_heap_usage());
    Account *myAccount = custom_malloc(sizeof(Account));  // heap allocation using custom_malloc
    if (myAccount == NULL) {
        fprintf(stderr, "Allocation failed\n");
        exit(1);
    }
    assert_heap_address(myAccount);  // ensure the heap address matches the last allocated address
    myAccount->id = 1;
    myAccount->balance = 1000.50;
    printf("Account on Heap - ID: %d, Balance: %.2f\n", myAccount->id, myAccount->balance);
    printf("Heap usage after allocation: %zu bytes\n", get_current_heap_usage());
    custom_free(myAccount, sizeof(Account));  // free heap memory using custom_free
    printf("Heap usage after free: %zu bytes\n", get_current_heap_usage());
}

void modifyAccountValue(Account acc) {
    acc.id = 2;
    acc.balance = 2000.00;
    printf("Modified Account by Value - ID: %d, Balance: %.2f\n", acc.id, acc.balance);
}

void modifyAccountReference(Account *acc) {
    acc->id = 3;
    acc->balance = 3000.00;
    printf("Modified Account by Reference - ID: %d, Balance: %.2f\n", acc->id, acc->balance);
}

size_t get_current_heap_usage() {
    return current_heap_usage;
}
