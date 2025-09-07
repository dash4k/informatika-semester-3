def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def sort(arr: list, low: int, high: int) -> None:
    if low < high:
        pivot = partition(arr, low, high)
        sort(arr, low, pivot - 1)
        sort(arr, pivot + 1, high)