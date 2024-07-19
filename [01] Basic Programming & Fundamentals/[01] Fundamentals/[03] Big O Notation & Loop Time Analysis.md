
# 📌 Big O Notation & Loop Time Analysis

View it in Detail here: [Big O Notation Tutorial](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)

## Overview
Big O notation is a powerful tool used in computer science to describe the time complexity or space complexity of algorithms. It provides a standardized way to compare the efficiency of different algorithms in terms of their worst-case performance.

**Big-O**, commonly referred to as **“Order of”**, is a way to express the **upper bound** of an algorithm’s time complexity, since it analyses the **worst-case** situation of algorithm. It provides an **upper limit** on the time taken by an algorithm in terms of the size of the input.

Time Taken Example: c<sub>1</sub>n<sup>2</sup> + c<sub>2</sub>n + c<sub>3</sub>

Big O Time Complexity: O(n<sup>2</sup>)

`Note: Therefore we usually consider the worst case i.e. highest order which n^2 and ignore the lower powers.`

Ignore the coefficient, even if it is n/2. Complexity is still written as O(n)

## Analyse Loops for Complexity Analysis of Algorithms
The analysis of loops for the complexity analysis of algorithms involves finding the number of operations performed by a loop as a function of the input size. This is usually done by determining the number of iterations of the loop and the number of operations performed in each iteration.

### 1. Constant Time Complexity O(1):
The time complexity of a function (or set of statements) is considered as `O(1)` if it doesn’t contain a loop, recursion, and call to any other non-constant time function. 

Examples for `O(1)` statements:
```python
- count = 0
- i = N
- count += i
- i /= 2 
```

### 2. Linear Time Complexity O(n):
The Time Complexity of a loop is considered as `O(n)` if the loop variables are incremented/decremented by a constant amount. For example following functions have `O(n)` time complexity. Linear time complexity, denoted as `O(n)`

Examples for `O(n)` statements:
```python
- for i in range(1, n+1, c): // O(n) expression
     # some O(1) expressions
 
- for i in range(n, 0, -c): // O(n) expression
     # some O(1) expressions
```

### 3. Quadratic Time Complexity O(nc):
The time complexity is defined as an algorithm whose performance is directly proportional to the squared size of the input data, as in nested loops it is equal to the number of times the innermost statement is executed.

An example of an `O(n^2)` algorithm is a nested loop that iterates over the entire input for each element, performing a constant amount of work for each iteration. This results in a total of `n * n` iterations, making the running time quadratic in the size of the input.

Examples for `O(n^2)` statements:
```python
- for i in range(1, n+1, c):
      for j in range(1, n+1, c):
          # some O(1) expressions
  
- for i in range(n, 0, -c):
      for j in range(i+1, n+1, c):
          # some O(1) expressions
```

### 4. Logarithmic Time Complexity O(Log n):
The time Complexity of a loop is considered as `O(Logn)` if the loop variables are divided/multiplied by a constant amount. And also for recursive calls in the recursive function, the Time Complexity is considered as `O(Logn)`.

Examples for `O(Logn)` statements:
```python
 - i = 1
    while(i <= n):
       i = i*c
 
 - i = n
    while(i > 0):
       i = i//c
 - # Recursive function
    def recurse(n):
        if(n <= 0):
            return
        else:
            # some O(1) expressions
        recurse(n/c)
    # Here c is positive integer constant greater than 1

```

### 5. Logarithmic Time Complexity O(Log Log n):
The Time Complexity of a loop is considered as `O(LogLogn)` if the loop variables are reduced/increased exponentially by a constant amount.
It uses exponents like i<sup>c</sup>, i<sup>1/2</sup> [sqrt], i<sup>2</sup>, etc.

Examples for `O(LogLogn)` statements:
```python
- # Here c is a constant greater than 1
  i = 2
  while(i <= n):
      # some O(1) expressions
      i = i**c
  
- # Here fun is sqrt or cuberoot or any other constant root
  i = n
  while(i > 1):
      # some O(1) expressions
      i = fun(i)

```
## Combine the time complexities of consecutive loops
For example, consider the following code:
```python
for i in range(n):
  for j in range(m):
    # some constant time operation
```
Here, the outer loop performs `n iterations`, and the inner loop performs `m iterations` for each iteration of the outer loop. So, the total number of iterations performed by the inner loop is `n * m`, and the total time complexity is `O(n * m)`.

In another example, consider the following code:
```python
for i in range(n):
  for j in range(i):
    # some constant time operation
```

Here, the outer loop performs `n iterations`, and the inner loop performs `i iterations` for each iteration of the outer loop, where i is the current iteration count of the outer loop. The total number of iterations performed by the inner loop can be calculated by summing the number of iterations performed in each iteration of the outer loop, which is given by the formula sum(i) from i=1 to n, which is equal to n * (n + 1) / 2. Hence, the total time complex

Another **Important thing, Combining Nested Loops**
```python
for i in range(n):
  for j in range(n/2):
    # some constant time operation
```
Outer loop gives `O(n)` * Inner loop gives `O(Logn)`.

`Results in O(nLogn)`

## Order of Growth for Multiple Loops
Subsequent but not nested loops,
```python
for i in range(n):
  for j in range(n):
    # some constant time operation
for i in range(n):
  for j in range(n/2):
    # some constant time operation
for l in range(n):
  # some constant time operation
for l in range(n*2):
  # some constant time operation
```

For Multiple Subsequent Loops one after the other, we simply add all the complexity:
`O(n^2)+ O(nLogn) + O(n) + O(Logn)`
Ignore the lower order terms and just consider the highest order term, i.e. `Time Complexity: O(n^2)`


## Different Inputs along with Subsequent Loops
```python
for i in range(m):
  for j in range(m):
    # some constant time operation
for i in range(n):
  for j in range(n/2):
    # some constant time operation
```
For Multiple Subsequent Loops one after the other, we simply add all the complexity: `O(m^2)+ O(nLogn)`.
Here, we cannont consider the highest order since there are 2 different variables. 

`Therefore, Overall Time Complexity is O(m^2)+ O(nLogn).`