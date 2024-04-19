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