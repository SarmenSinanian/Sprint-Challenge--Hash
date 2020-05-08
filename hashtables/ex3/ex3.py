def intersection(arr):
    nums = {}
    result = []
    arr = sorted(arr, key=lambda x: len(x))
    for i in arr[0]:
        nums[i] = 1
    for i in arr[1:]:
        for n in i:
            if n in nums:
                nums[n] += 1
    result = [a for a in nums if nums[a] == len(arr)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))