def pickingNumbersContigous(arr): #learn to read
    longest_subarray_len = 0
    current_subarray_len = 0
    diff = 0

    print(arr)

    for i in range(len(arr)):
        if (arr[i - current_subarray_len]) == arr[i]: #equal to first
            current_subarray_len += 1
        elif arr[i - current_subarray_len] + diff == arr[i]: #+/- 1 first (if diff set)
            current_subarray_len += 1
        elif current_subarray_len >= 1 and abs(arr[i - current_subarray_len] - arr[i]) == 1 and diff == 0:
            diff = arr[i] - arr[i - current_subarray_len] 
            current_subarray_len += 1
        else:
            if current_subarray_len > longest_subarray_len:
                longest_subarray_len = current_subarray_len
            current_subarray_len = 1
            diff = 0

        if current_subarray_len > longest_subarray_len:
            longest_subarray_len = current_subarray_len

    return longest_subarray_len


def pickingNumbers(arr):
    arr.sort()
    return pickingNumbersContigous(arr)


print(pickingNumbers([1, 2, 2, 3, 1, 2, 4, 2]))
print(pickingNumbers([4, 6, 5, 3, 3, 1]))
print(pickingNumbers([2, 2]))