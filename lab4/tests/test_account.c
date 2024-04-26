#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "../include/account.h"

void test_account_on_stack() {
    Account myAccount;  // test account creation on stack
    myAccount.id = 1;
    myAccount.balance = 1000.50;
    assert(myAccount.id == 1 && myAccount.balance == 1000.50);  // verification
}

void test_account_on_heap() {
    Account *myAccount = malloc(sizeof(Account));  // test account creation on heap
    assert(myAccount != NULL);
    myAccount->id = 1;
    myAccount->balance = 1000.50;
    assert(myAccount->id == 1 && myAccount->balance == 1000.50);  // verification
    free(myAccount);
}

void test_modify_account_value() {
    Account myAccount = {1, 1000.50};
    modifyAccountValue(myAccount);
    assert(myAccount.id == 1 && myAccount.balance == 1000.50);  // verifies no change to original
}

void test_modify_account_reference() {
    Account myAccount = {1, 1000.50};
    modifyAccountReference(&myAccount);
    assert(myAccount.id == 3 && myAccount.balance == 3000.00);  // verifies changes by reference
}

int main() {
    test_account_on_stack();
    test_account_on_heap();
    test_modify_account_value();
    test_modify_account_reference();
    printf("All tests passed successfully!\n");
    return 0;
} 