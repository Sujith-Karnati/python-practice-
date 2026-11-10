def two_numbers(lis,target):
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i]+lis[j] == target:
                return((i,j))
    return None 
print(two_numbers([2, 7, 11, 15],9))
print(two_numbers([3, 2, 4],6))
print(two_numbers([3, 3],6))
print(two_numbers([1,5,8,10],20))


def two_numbers(lis, target):
    seen = {}
    for i in range(len(lis)):
        num = lis[i]
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return None
print(two_numbers([2, 7, 11, 15], 9))
print(two_numbers([3, 2, 4], 6))
print(two_numbers([3, 3],6))
print(two_numbers([1,5,8,10],20))