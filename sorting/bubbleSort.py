import time
# array = [4,5,7,6,2,1]
# array1 = [1,2,3,4,5,6]

def sorting(arr):
    for i in range(len(arr)-1,0,-1):
        swaped = False 
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                swaped = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            
            # print(arr)
        if not swaped:
            break

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
time_taken = end_time - start_time
print("Time taken for sorting = ",time_taken)



 
