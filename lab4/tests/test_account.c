#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "../include/account.h"

void test_account_on_stack() {
    Account myAccount;
    myAccount.id = 1;
    myAccount.balance = 1000.50;
    assert(myAccount.id == 1);
    assert(myAccount.balance == 1000.50); 
}

void test_account_on_heap() {
    Account *myAccount = malloc(sizeof(Account));
    assert(myAccount != NULL);  
    myAccount->id = 1;
    myAccount->balance = 1000.50;
    assert(myAccount->id == 1);
    assert(myAccount->balance == 1000.50);  
    free(myAccount);
}

int main() {
    test_account_on_stack();
    test_account_on_heap();
    printf("All tests passed successfully!\n");
    return 0;
}

