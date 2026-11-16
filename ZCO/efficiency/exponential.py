def all_subsets(arr):
    subsets = [[]]
    for item in arr:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset)
            new_subsets.append(subset + [item])
        subsets = new_subsets
    return subsets 