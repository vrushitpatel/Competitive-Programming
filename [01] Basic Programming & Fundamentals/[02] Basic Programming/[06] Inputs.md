
# 📌 Python List Methods

View it in Detail here: [Python Tutorial](https://www.w3schools.com/python/python_user_input.asp)

## Python User Input
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.
- Python 3.6 uses the `input()` method.
- Python 2.7 uses the `raw_input()` method.

The following example asks for the username, and when you entered the username, it gets printed on the screen:
```python
username = input("Enter username:")
print("Username is: " + username)
```
```python
username = raw_input("Enter username:")
print("Username is: " + username)
```
```
Note: Python stops executing when it comes to the input() function, and continues when the user has given some input.
```

## How to take Integer Input in Python?
```python
input_a = input()
print(type(input_a)) # <class 'str'>

# type cast into integer
input_a = int(input_a)
print(type(input_a)) # <class 'int'>
```
```python
# integer input
input_b = int(input())
print(type(input_b)) # <class 'int'>
```
## How to take List Input in Python?
### Method 1: Using Loops
```python
# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)  
 
print(lst)
```
```python
# Output:-
Enter number of elements : 5
12
33
0
5
13
[12, 33, 0, 5, 13]
```
- Time Complexity: O(n), where n is the length of the list.
- Auxiliary Space: O(n) additional space of size n is created where n is the number of elements in the list 

### Method 2: With Exception Handling  
```python
# try block to handle the exception
try:
    my_list = []
 
    while True:
        my_list.append(int(input()))
 
# if the input is not-integer, just print the list
except:
    print(my_list)
```
```python
# Output:-
Enter number of elements : 
12
33
0
5
13
56
33
Stop
[12, 33, 0, 5, 13, 56, 33]
```
### Method 3: Using Map()  
```python
# number of elements
n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
a = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]
 
print("\nList is - ", a)
```
```python
# Output:-
Enter number of elements : 5
Enter the numbers: 3 15 22 18 33
List is - [12, 33, 0, 5, 13, 56, 33]
```
### Method 4: Accepting Elements as String, Space Seperated
```python
# User Input Space Seperated
inputList = list(input("Enter the List (Space Seperated): ").split(' '))
 
print("Original List is: ", inputList)
```
```python
# Output:-
Enter number of elements : 5
Enter the numbers: 3 15 22 18 33
List is - [12, 33, 0, 5, 13, 56, 33]
```
### Method 5: List of lists as input   
```python
lst = []
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = [input(), int(input())]
    lst.append(ele)
 
print(lst)
```
```python
# Output:-
Enter number of elements : 3
Geeks
3
For
7
Geeks
9
List is - [['Geeks', 3], ['For', 7], ['Geeks', 9]]
```
### Method 6: Using List Comprehension and Typecasting [Best Method]
```python
# For list of integers
lst1 = []
 
# For list of strings/chars
lst2 = []
 
lst1 = [int(item) for item in input("Enter \
                the list items : ").split()]
 
lst2 = [item for item in input("Enter \
                the list items : ").split()]
 
print(lst1)
print(lst2)
```
```python
# Output:-
Enter the list 1 items : 3 2 4 1 0 6 7
Enter the list 2 items : ABC DEF GHI
Output:
[3, 2, 4, 1, 0, 6, 7]
['ABC', 'DEF', 'GHI']
```