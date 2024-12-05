def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

def quick_sort(array):
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
    
    sort(array, 0, len(array) - 1)

def count_sort(input_array):
    M = max(input_array)
    count_array = [0] * (M + 1)

    for num in input_array:
        count_array[num] += 1

    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(input_array)

    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1

    return output_array

def bucket_sort(arr: list) -> None:
    min_value, max_value = min(arr), max(arr)
    data_range = max_value - min_value

    bucket_count = len(arr) // 5 or 1
    bucket_range = data_range / bucket_count

    buckets = [[] for _ in range(bucket_count + 1)]

    for item in arr:
        i = int((max_value - min_value) // bucket_range)
        buckets[i].append(item)

    output = []

    for bucket in buckets:
        output.extend(sorted(bucket))

    return output