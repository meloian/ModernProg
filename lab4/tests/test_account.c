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

void test_modify_account_value() {
    Account myAccount = {1, 1000.50};
    modifyAccountValue(myAccount);
    assert(myAccount.id == 1);
    assert(myAccount.balance == 1000.50);
}

void test_modify_account_reference() {
    Account myAccount = {1, 1000.50};
    modifyAccountReference(&myAccount);
    assert(myAccount.id == 3);
    assert(myAccount.balance == 3000.00);
}

int main() {
    test_account_on_stack();
    test_account_on_heap();
    test_modify_account_value();
    test_modify_account_reference();
    printf("All tests passed successfully!\n");
    return 0;
} 

