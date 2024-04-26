#include <stdio.h>
#include <stdlib.h>
#include "../include/account.h"

void createAndDisplayAccountOnStack() {
    Account myAccount;  // stack allocation
    myAccount.id = 1;
    myAccount.balance = 1000.50;
    printf("Account on Stack - ID: %d, Balance: %.2f\n", myAccount.id, myAccount.balance);
}

void createAndDisplayAccountOnHeap() {
    Account *myAccount = malloc(sizeof(Account));  // heap allocation
    if (myAccount == NULL) {
        fprintf(stderr, "Allocation failed\n");
        exit(1);
    }
    myAccount->id = 1;
    myAccount->balance = 1000.50;
    printf("Account on Heap - ID: %d, Balance: %.2f\n", myAccount->id, myAccount->balance);
    free(myAccount);  // free heap memory
}

void modifyAccountValue(Account acc) {
    acc.id = 2; // changes won't affect original as it's a copy
    acc.balance = 2000.00;
    printf("Modified Account by Value - ID: %d, Balance: %.2f\n", acc.id, acc.balance);
}

void modifyAccountReference(Account *acc) {
    acc->id = 3;  // directly modifies the original account
    acc->balance = 3000.00;
    printf("Modified Account by Reference - ID: %d, Balance: %.2f\n", acc->id, acc->balance);
}
