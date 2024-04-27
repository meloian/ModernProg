#include <stdio.h>
#include <stdlib.h>
#include "../include/account.h"

static size_t current_heap_usage = 0;

void* custom_malloc(size_t size) {
    void* ptr = malloc(size);
    if (ptr) {
        current_heap_usage += size;
    }
    return ptr;
}

void custom_free(void* ptr, size_t size) {
    if (ptr) {
        free(ptr);
        current_heap_usage -= size;
    }
}

void createAndDisplayAccountOnStack() {
    Account myAccount;  // stack allocation
    myAccount.id = 1;
    myAccount.balance = 1000.50;
    printf("Account on Stack - ID: %d, Balance: %.2f\n", myAccount.id, myAccount.balance);
}

void createAndDisplayAccountOnHeap() {
    Account *myAccount = custom_malloc(sizeof(Account));  // heap allocation using custom_malloc
    if (myAccount == NULL) {
        fprintf(stderr, "Allocation failed\n");
        exit(1);
    }
    myAccount->id = 1;
    myAccount->balance = 1000.50;
    printf("Account on Heap - ID: %d, Balance: %.2f\n", myAccount->id, myAccount->balance);
    custom_free(myAccount, sizeof(Account));  // free heap memory using custom_free
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
