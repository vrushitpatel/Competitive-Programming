# 📌 Python List Methods

## Time Complexity (Big O Notation):

| Method                                     | Description                                                                                                                                         | Time Complexity |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Accessing an element (indexing)            | Constant time, as elements are stored contiguously in memory and can be accessed directly by their index.                                           | O(1)            |
| Appending an element (append())            | While sometimes a list might need to resize and copy elements to a new, larger memory location, on average, appending is a constant-time operation. | O(1)            |
| Inserting an element (insert())            | Linear time, as all subsequent elements need to be shifted to make space for the new element.                                                       | O(n)            |
| Deleting an element (del, pop(), remove()) | Linear time, as elements after the deleted element need to be shifted to fill the gap.                                                              | O(n)            |
|                                            | pop() without an index is O(1) as it removes the last element.                                                                                      | O(1)            |
| Iteration                                  | Linear time, as each element in the list is visited once.                                                                                           | O(n)            |
| Slicing                                    | where k is the length of the slice - Linear time, as a new list needs to be created and elements copied.                                            | O(k)            |
| Checking for containment (in operator)     | Linear time, as the list needs to be traversed sequentially in the worst case.                                                                      | O(n)            |
| len()                                      | Constant time, as the length is typically stored as an attribute of the list object.                                                                | O(1)            |
| sort()                                     | Python's In-Built Sort Function                                                                                                                     | O(n log n)      |

## Space Complexity (Big O Notation):

| Method                              | Description                                                                                                                                                             | Space Complexity |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Storing elements                    | Linear space, as the memory used grows proportionally with the number of elements in the list.                                                                          | O(n)             |
| Creating a copy (copy() or slicing) | Linear space, as a new list of the same size is created.                                                                                                                | O(n)             |
| Extending a list (extend())         | where k is the length of the list being appended - Linear space, as the new elements are added to the existing list, potentially requiring a resize and copy operation. | O(k)             |
