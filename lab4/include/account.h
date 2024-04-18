#ifndef ACCOUNT_H
#define ACCOUNT_H

typedef struct {
    int id;
    double balance;
} Account;

void createAndDisplayAccountOnStack();
void createAndDisplayAccountOnHeap();
void modifyAccountValue(Account acc);  
void modifyAccountReference(Account *acc);  

#endif
