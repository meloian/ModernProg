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

#endif
