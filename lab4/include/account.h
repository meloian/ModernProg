#ifndef ACCOUNT_H  // prevents the file from being included multiple times
#define ACCOUNT_H

typedef struct {
    int id;
    double balance;
} Account;  // defines a structure to hold account data

// function prototypes for managing accounts
void createAndDisplayAccountOnStack();
void createAndDisplayAccountOnHeap();
void modifyAccountValue(Account acc);  
void modifyAccountReference(Account *acc);  

void* custom_malloc(size_t size);
void custom_free(void* ptr, size_t size);
size_t get_current_heap_usage();
void assert_heap_address(void *ptr);  // says the allocated memory address is the last known heap address.

#endif
