def bubble_sort(arr: list) -> None:
    l = len(arr)
    for i in range(l):
        swapped = False
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

f = [0,22,1,43,2,4,5]
bubble_sort(f)
print(f)