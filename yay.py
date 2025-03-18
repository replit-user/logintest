from time import sleep
from random import randint
from random import choice
def sort(arr:list[int]) -> list[int]:
    elems = []
    for elem in arr:
        elems.append(elem)
        elems.sort()
        print(elems,"\n")
        sleep(0.5)
    return elems



def wierd_sort(arr: list[int]) -> list[int]:
    pivot = choice(arr)
    big = []
    small = []
    for elem in arr:
        if elem > pivot:
            big.append(elem)
            print(big, "\n")
            sleep(0.5)
        else:
            small.append(elem)
            print(small, "\n")
            sleep(0.5)
        sleep(0.5)
    big = sort(big)
    small = sort(small)
    small.extend(big)
    sleep(0.5)
    print("Sorted array: ", small)
    return small

    
def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr, "\n")
        sleep(0.5)
    return arr


#and here

size = 10

array = [randint(1,1000) for _ in range(size)]

algorithms = {
    "instantort":sort,
    "wierd sort":wierd_sort,
    "bubble sort": bubble_sort,
    #add algorithms here
}

for algorithm in algorithms:
    option = input(f"Choose {algorithm} (Y/N): ")
    if option.lower() == 'y':
        chosen = algorithms[algorithm]
        break

print("Original array: ", array)


chosen(array)