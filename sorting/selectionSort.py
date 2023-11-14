import time
# array = [2,4,5,1,6,3]
# array1 =[50,10,25,30,45]
# array2 =[-5,-8,-1,0,2,-6]
# array3 =[1,2,3,4,5,6]

def sorting(arr):
    for i in range(0,len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
            # print(arr)
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

n = int(input())
arr1 = []
for _ in range(n):
    i = int(input())
    arr1.append(i)
    
start_time = time.time()
print(start_time)
sorting(arr1)
end_time = time.time() 
print(end_time)
# print(array) 
time_taken = end_time - start_time
print("Time taken for sorting = ",time_taken)

