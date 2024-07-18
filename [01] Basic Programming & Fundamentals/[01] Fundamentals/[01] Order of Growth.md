
# 📌 Order of Growth

View it in Detail here: [Analyse Loops for Complexity](https://www.geeksforgeeks.org/how-to-analyse-loops-for-complexity-analysis-of-algorithms/)

## Overview
Order of growth is how the time of execution depends on the length of the input. Consider the highest order in the expresion & remove the lower order.

Time Taken Example: c<sub>1</sub>n<sup>2</sup> + c<sub>2</sub>n + c<sub>3</sub>

Worst Case: O(n<sup>2</sup>)

`Note: Therefore we usually consider the worst case i.e. highest order which n^2 and ignore the lower powers.`

Ignore the coefficient, even if it is n/2. Complexity is still written as O(n)

### Example
Let’s calculate the time complexity of the below algorithm:

```
count = 0
i = N
while(i > 0):
  for j in range(i):
    count+=1
  i /= 2
```
This is a tricky case. In the first look, it seems like the complexity is O(N * log N). N for the j′s loop and log(N) for i′s loop. But it’s wrong. Let’s see why.

Think about how many times count++ will run. 

When i = N, it will run N times.
When i = N / 2, it will run N / 2 times.
When i = N / 4, it will run N / 4 times.
And so on.
The total number of times count++ will run is N + N/2 + N/4+…+1= 2 * N. So the time complexity will be O(N).

## Order of Growth

`Remember this:`

constant < log(log(n)) < log(n) < n<sup>1/3</sup> < n<sup>1/2</sup> < n < n<sup>2</sup> < n<sup>3</sup> < n<sup>4</sup> < 2<sup>n</sup> < n<sup>n</sup> < n!
