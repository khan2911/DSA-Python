  # sum(array(0, n))    = array[0] + array[1] +...... + array[n]
#                     = sum(array(0, n-1)) + array[n]

def arraysum(arr,n):
    if n < 1 :
        return 1
    if arr[n-1] == 0:
        return 0
    return (arr[n-1]) * arraysum(arr,n-1)
   
    

arr1 = [1,2,3,4,5,6,8]
print(arraysum(arr1,len(arr1)))


# arraysum([1,2,3,4,5], 5)
#     arraysum([1,2,3,4,5], 4) + 5
#         arraysum([1,2,3,4,5], 3) + 4 + 5
#             arraysum([1,2,3,4,5], 2) + 3 + 4 + 5
#                 arraysum([1,2,3,4,5], 1) + 2 + 3 + 4 + 5
#                     arraysum([1,2,3,4,5], 0) + 1 + 2 + 3 + 4 + 5
#                         0 + 1 + 2 + 3 + 4 + 5

# arraysum([1,2,3,4,5],5)
#          arraysum([1,2,3,4,5],4)*5
#               arraysum([1,2,3,4,5],3)*4*5
#               arraysum([1,2,3,4,5],2)3*4*5
#                   arraysum([1,2,3,4,5],1)2*3*4*5
#                    0*1*2*3*4*5  
