#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "../include/account.h"

extern size_t get_current_heap_usage();  // declare external function to get heap usage

void test_account_on_stack() {
    size_t initial_heap = get_current_heap_usage();
    Account myAccount;  // test account creation on stack
    myAccount.id = 1;
    myAccount.balance = 1000.50;
    size_t final_heap = get_current_heap_usage();
    assert(initial_heap == final_heap);  // ensure no change in heap usage
    assert(myAccount.id == 1 && myAccount.balance == 1000.50);  // verification
}

void test_account_on_heap() {
    size_t initial_heap = get_current_heap_usage();
    Account *myAccount = custom_malloc(sizeof(Account));  // test account creation on heap
    assert(myAccount != NULL);
    myAccount->id = 1;
    myAccount->balance = 1000.50;
    size_t final_heap = get_current_heap_usage();
    assert(final_heap == initial_heap + sizeof(Account));  // ensure increased heap usage
    assert(myAccount->id == 1 && myAccount->balance == 1000.50);  // verification
    custom_free(myAccount, sizeof(Account));
    assert(get_current_heap_usage() == initial_heap);  // ensure heap is back to initial after free
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