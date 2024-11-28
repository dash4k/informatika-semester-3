def sort(arr: list) -> None:
    l = len(arr)
    for i in range(l):
        min_val = i
        for j in range(i + 1, l):
            if arr[j] < arr[min_val]:
                min_val = j
        arr[i], arr[min_val] = arr[min_val], arr[i]