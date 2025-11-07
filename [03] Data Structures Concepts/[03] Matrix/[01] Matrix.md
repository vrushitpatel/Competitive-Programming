# 📌 Python Lists Operations

View it in Detail here: [Matrix Python Tutorial](https://www.scaler.com/topics/2d-array-in-python/)

## Overview

A 2D array in Python is a nested data structure, meaning it is a set of arrays inside another array. The 2D array is mostly used to represent data in a tabular or two-dimensional format.

- Initializing 2D Array
- Accessing Values
- Traversing Values in Python 2D Array
- Inserting Values in Python 2D Array
- Updating Values in Python 2D Array
- Deleting Values in Python 2D Array

### Initializing 2D Array

Where array_name is the array's name, n_rows is the number of rows in the array, and n_columns is the number of columns in the array.

```python
array_name=[n_rows][n_columns]

OR

array_name = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
```

### Accessing Values

It can be done by using the row and column indices of the element to be accessed. It has the following syntax:

```python
array_name[row_ind][col_ind]

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[1][2]) # 10
```

If we specify only one index while accessing an array, this index is treated as the row index, and the whole row is returned. It has the syntax:

```python
array_name[row_ind]

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0]) # [11, 12, 5, 2]
```

### Traversing Values in Python 2D Array

Traversing means sequentially accessing each value of a structure. Traversing in a 2D array in python can be done by using a for a loop.

```python
arr=[[1,2,3],[4,5,6],[7,8,9]]

for r in arr:
    for c in r:
        print(c, end = " ")
    print()
```

Output:

```
1 2 3
4 5 6
7 8 9
```

## Inserting Values in Python 2D Array

### Adding a New Element in the Outer Array.

This can be done by using the .insert() method of the array module in python; thus, we need to import the array module. The insert method has the following syntax:

```python
arr1.insert(ind,arr_insert)
------------------------------
from array import *

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i, end=" ")
    print()


arr.insert(2, [11, 12, 13])

print("Modified Array")
for _ in arr:
    for i in _:
        print(i, end=" ")
    print()

```

Output:

```
Original Array
1 2 3
4 5 6
7 8 9
Modified Array
1 2 3
4 5 6
11 12 13
7 8 9

```

### Adding a New Element in the Inner Array.

This can be done using the .insert() method of the array module in python; thus, we need to import the array module. In this case, instead of adding a value to the outer array, we add it to the inner array and thus specify the index of the array element where inside which the element will be added. Here we use the syntax as:

```python
arr1[r].insert(ind,arr_insert)
------------------------------
from array import *

arr=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()

arr[1].insert(2,12)

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()

```

Output:

```
Original Array
1 2 3
4 5 6
7 8 9
Modified Array
1 2 3
4 5 12 6 
7 8 9

```

## Updating Values in Python 2D Array

### Updating a Single Element

We can update a single element in a 2D array by specifying its row and column index and assigning that array position a new value. Assigning a new value overwrites the old value, thus updating it.

```python
arr_name[r][c]=new_element
---------------------------
arr=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()

arr[1][2]=16

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()
```

Output:

```
Original Array
1 2 3
4 5 6
7 8 9
Modified Array
1 2 3
4 5 16
7 8 9
```

### Updating an Inner Array

We can also update an array inside our outer array. This can be done by specifying its index in the outer array and then assigning that array position a new array.

```python
arr_name[ind]=new_array
------------------------
arr=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()
new_arr=[10,11,12]
arr[1]=new_arr

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()
```

Output:

```
Original Array
1 2 3
4 5 6
7 8 9
Modified Array
1 2 3
10 11 12
7 8 9
```

## Deleting Values in Python 2D Array

### Deleting a Single Element

We can delete a single element in a 2D array by specifying its row and column index and applying the del() method on it.

```python
del(arr_name[r][c])
--------------------
from array import *
arr=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()

del(arr[1][2])

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()
```

Output:

```
Original Array
1 2 3
4 5 6
7 8 9
Modified Array
1 2 3
4 5
7 8 9
```

### Deleting an Entire Inner Array

We can also delete a complete array from the outer array. This can be done by applying the del method on an array element of the outer array by specifying only the inner array's index.

```python
del(arr_name[ind])
--------------------
from array import *
arr=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()

del(arr[1])

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()
```

Output:

```
Original Array
1 2 3
4 5 6
7 8 9
Modified Array
1 2 3
7 8 9
```
