def insertion_sort(arr: list) -> None:
    l = len(arr)
    for i in range(1, l):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = temp

f = [0,22,1,43,2,4,5]
insertion_sort(f)
print(f)