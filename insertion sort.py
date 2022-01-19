def insertionSort(arr):

    for i in range(1,len(arr)):

        key=arr[i]

        j=i-1
        while j>=0 and key<arr[j]:
            arr [j+1] = arr[j]
            j-=1
        arr[j+1]=key


arr=[12, 11, 13, 15, 14, 19, 17, 16, 20, 10, 3, 5, 7, 1, 4, 2, 6, 9, 8, 18]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])