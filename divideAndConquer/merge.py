import time
def merge(arr1,arr2):
    mergedArr= []
    i=0
    j=0
    while i<len(arr1) and j<len(arr2) :
        if arr1[i]<arr2[j]:
            mergedArr.append(arr1[i])
            i+=1
        else:
            mergedArr.append(arr2[j])
            j+=1

    while i< len(arr1):
        mergedArr.append(arr1[i])
        i+=1
    
    while j< len(arr2):
        mergedArr.append(arr2[j])
        j+=1
    return mergedArr

# arr1 = [1,3,5,7,9,10,12,13,14,15,17]
# arr2 = [2,4,6,8,11,16,18,19,20,21,23,24]
# print(merge(arr1,arr2))


def sort(arr,l, r):
    
    if l >= r :
        return [arr[l]]
    mid = (l+r-1)//2
    a = sort(arr,l,mid)
    b = sort(arr,mid+1,r)
    
    return merge(a,b)
# arr1 = [5,3,2,6,1,7,8,9,4]
n = int(input())
arr1 = []
for _ in range(n):
    i = int(input())
    arr1.append(i)

start_time = time.time()
print(start_time)
# print(sort(arr1,0,len(arr1)-1))
end_time = time.time()
print(end_time)
time_taken = end_time - start_time
print("Time taken for sorting = ",time_taken)