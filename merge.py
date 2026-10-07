import random
comparisons = 0
def merge(arr, left, mid, right):
    global comparisons
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        comparisons += 1                  
        if L[i] <= R[j]:
            arr[k] = L[i]; i += 1
        else:
            arr[k] = R[j]; j += 1
        k += 1

    while i < len(L):                     
        arr[k] = L[i]; i += 1; k += 1
    while j < len(R):
        arr[k] = R[j]; j += 1; k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)       
        merge_sort(arr, mid + 1, right)  
        merge(arr, left, mid, right)      

def count_comparisons(data):
    global comparisons
    comparisons = 0
    arr = data[:]
    merge_sort(arr, 0, len(arr) - 1)
    return comparisons

if __name__ == "__main__":
    n = 16
    sorted_ages  = list(range(1, n + 1))                 
    reverse_ages = list(range(n, 0, -1))                 
    random_ages  = [random.randint(1, 90) for _ in range(n)] 

    print("Sample random ages:", random_ages)
    s = random_ages[:]
    merge_sort(s, 0, len(s) - 1)
    print("Sorted ages       :", s)


    print(f"\n{'n':>6} {'Sorted':>10} {'Reverse':>10} {'Random':>10}")
    for n in [8, 16, 100, 1000, 10000]:
        a = list(range(n))
        b = list(range(n, 0, -1))
        c = [random.randint(1, 90) for _ in range(n)]
        print(f"{n:>6} {count_comparisons(a):>10} {count_comparisons(b):>10} {count_comparisons(c):>10}")