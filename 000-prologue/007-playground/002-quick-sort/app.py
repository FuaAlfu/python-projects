def QuickSortArray(arr):
    elements = len(arr)
    if elements < 2:
        return arr
    
    current_position = 0;

    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    left = QuickSortArray(arr[0:current_position]) 
    right = QuickSortArray(arr[current_position+1:elements]) 

    arr = left + [arr[current_position]] + right
    
    return arr



my_array = [77,453,2,60,398,44,87,19,39,5,123]
print("my Array: ",my_array)
print("quick sort: ",QuickSortArray(my_array))