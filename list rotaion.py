def list_rotation(list,k):
    n = len(list)
    k = k % n  # Handle cases where k is greater than the length of the list
    return list[-k:] + list[:-k]
print(list_rotation([1,2,3,4],2))