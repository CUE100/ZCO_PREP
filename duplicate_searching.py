arr_found=[]

def has_duplicate(arr):
    for x in arr:
        if x not in arr_found:
            arr_found.append(x)
        else:
            return True