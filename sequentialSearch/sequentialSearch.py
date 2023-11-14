aray = [10,20,52,62,44]
def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
           return i
    
    return -1
print(search(aray,62))    


