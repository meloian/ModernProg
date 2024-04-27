# Short Research

In C, data can be passed by value and by reference. Passing by value creates a copy of the data, so changes are made to the copy, not the original. This is similar to value types in higher-level languages.

C also allows reference passing using pointers. When we pass a memory address (pointer) to a function, we can change the object. These are not true reference types, but pointers allow similar behaviour.

But C does not have a built-in garbage collector. This means programmers have to manage memory themselves, using functions like `malloc` to allocate and free memory. If this is not done correctly, errors can occur.

## Value Types and Reference Types

The project uses passing by value and by reference. The `modifyAccountValue` function copies the Account structure, demonstrating passing by value. The `modifyAccountReference` function uses a pointer to a structure, allowing direct modification of the original object, simulating passing by reference.

## Objects on the Stack and Heap

### On the Stack
In the `createAndDisplayAccountOnStack` function, the object is created as a local variable inside the function. This means it disappears when the function ends.

### On the Heap
In the `createAndDisplayAccountOnHeap` function, memory is allocated using `malloc`. An object created on the heap stays available after the function ends. It can exist even if the function has restrictions.

## Testing Memory Allocation

I've added a way to track memory in our code. This is important for making sure objects are placed correctly on the stack or heap.

- **Stack Allocation Test (`test_account_on_stack`)**: Check how much memory is used before and after creating an object on the stack. If the object is correctly placed on the stack, the memory usage should not change. This is verified by checking that the heap usage difference (`delta`) is zero.

- **Heap Allocation Test (`test_account_on_heap`)**: Check how much memory is used before and after an object is allocated on the heap using `custom_malloc`. The heap usage should increase by the size of the object. After freeing the object with `custom_free`, the heap usage should return to its original state. This shows the object was allocated and freed correctly, with no memory leaks.