# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
# Maximum and Minimum of an Array
arr = [int(item) for item in input("Enter the List Items: ").split()]
print("User List: ", arr)
arr_min, arr_max = arr[0], arr[0]
for x in arr:
    if arr_min > x:
        arr_min = x
    elif arr_max < x:
        arr_max = x
print("Minimum Value: ", arr_min)
print("Maximum Value: ", arr_max)