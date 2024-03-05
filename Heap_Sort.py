count = 0
def max_heapify(array, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    global count
    if left < heap_size:
        count += 1
        if array[left] > array[largest]:
            largest = left
    if right < heap_size:
        count += 1
        if array[right] > array[largest]:
            largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heap_size, largest)

def build_heap(array):
    heap_size = len(array)
    for i in range ((heap_size//2),-1,-1):
        max_heapify(array,heap_size, i)

def heap_sort(array):
    heap_size = len(array)
    build_heap(array)
    print (f'Heap : {array}')
    for i in range(heap_size-1,0,-1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        max_heapify(array, heap_size, 0)

array = [5,9,3,10,45,2,0]
heap_sort(array)
print (array)
print(f'Number of comparisons = {count}')


sorted_array = [5,6,7,8,9]
heap_sort(sorted_array)
print(sorted_array)
print(f'Number of comparisons = {count}')

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
heap_sort(reverse_sorted_array)
print(reverse_sorted_array)
print(f'Number of comparisons = {count}')
