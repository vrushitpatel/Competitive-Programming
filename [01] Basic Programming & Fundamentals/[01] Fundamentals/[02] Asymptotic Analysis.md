# 📌 Asymptotic Analysis

- View it in Detail here: [Asymptotic Analysis](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)
- YouTube Playlist: [Analyzing Algorithms by Michael Sambol](https://youtube.com/playlist?list=PL9xmBV_5YoZMxejjIyFHWa-4nKg6sdoIv&si=_7p-xmDaIhvo-Byr)

## Overview

Asymptotic notation is a way to describe the running time or space complexity of an algorithm based on the input size. It is commonly used in complexity analysis to describe how an algorithm performs as the size of the input grows.

They are mathematical notation to represent order of growth of any function.

## Worst, Average and Best Case Analysis of Algorithms

- **1. Worst Case Analysis (Mostly used)**:
  In the worst-case analysis, we calculate the upper bound on the running time of an algorithm. We must know the case that causes a maximum number of operations to be executed.
- **2. Average Case Analysis (Rarely used)**:
  In the average case analysis, we must know (or predict) the mathematical distribution of all possible inputs.
- **3. Best Case Analysis (Very Rarely used)**:
  In the best-case analysis, we calculate the lower bound on the running time of an algorithm. We must know the case that causes a minimum number of operations to be executed.

## Types of Asymptotic Notation

The three most commonly used notations are Big O, Omega, and Theta. It applies to the Functions.

- **Big O notation (O)**: Exact or Upper Bound Order of Growth. It represents the worst-case scenario, i.e., the maximum amount of time or space an algorithm may need to solve a problem.
- **Theta notation (θ)**: Exact Order of Growth. Which describes a tight bound when the best and worst cases are the same, i.e., the amount of time or space an algorithm typically needs to solve a problem.
- **Omega notation (Ω)**: Exact or Lower Bound Order of Growth. It represents the best-case scenario, i.e., the minimum amount of time or space an algorithm may need to solve a problem.

### Example

```python
# Linearly search x in arr[]. If x is present
# then return the index, otherwise return -1

def search(arr, x):
    for index, value in enumerate(arr):
        if value == x:
            return index
    return -1

# Driver's Code
if __name__ == '__main__':
    arr = [1, 10, 30, 15]
    x = 30

    # Function call
    print(x, "is present at index",
          search(arr, x))
```

Time Complexity Analysis:

- **For Big O notation (O)**:
  ```
  Time Complexity is: O(n) // either n or lower
  ```
  But considering Upper Bound, we write O(n)
- **For Theta notation (θ)**:
  ```
  Time Complexity is:
      Worst Case: θ(n)
      Best Case : θ(1)
  ```
  Considering both the Worst and the Best Case.
- **For Omega notation (Ω)**:
  ```
  Time Complexity is: Ω(1) // Constant Flow
  ```
  But considering Lower Bound, it will not iterate and result in constant time.

`Note: Therefore we usually use Big O & Theta as we are interested more in Upper Bound (i.e. Worst Case) & Average Order of Growth.`
