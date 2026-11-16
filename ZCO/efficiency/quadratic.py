
def has_pair_sum(arr,target):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if x != y and arr[x] + arr[y] == target:
                return True
    return False