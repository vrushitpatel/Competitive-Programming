# https://www.geeksforgeeks.org/program-to-reverse-an-array/#2-array-reverse-using-a-loop-inplace
# Reversing an array
"""
Directly Coding in the VSCode:
    1. Write the Python Script with .py extension
    2. Take inputs using input("Enter your Name: ")
    3. In the Terminal go to the file path
    4. Run 'python file_name.py'
    5. Enter your inputs and get the output
"""
"""
# Method 1: No Extra Space
def revlist(inputList, start, end):
    while start < end:
        inputList[start], inputList[end] = inputList[end], inputList[start]
        start += 1
        end -= 1
"""
"""
# Method 2: Recursion Method
def revlist(inputList, start, end):
    while start >= end:
        return
    inputList[start], inputList[end] = inputList[end], inputList[start]
    revlist(inputList, start + 1, end - 1)
"""
inputList = [int(item) for item in input("Enter the List Items : ").split()]
print("Original List is: ", inputList)

# Method 1 & 2
"""
revlist(inputList, 0, len(inputList) - 1)
print("Reverse List is: ", inputList)
"""
# Method 3: Built-in Method
reversed_array = list(reversed(inputList))
print("Reverse List is: ", reversed_array)