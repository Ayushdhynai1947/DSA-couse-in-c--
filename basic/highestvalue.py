arr = [10, 22, 38,27,11]
temp = 0

print('elements of orignial array ')
for i in range(0,len(arr)):
    print(arr[i], end=" ")
    
    
    
for i in range (0,len(arr)):
    for j in range(i+1 , len(arr)):
        if(arr[i] >arr[j]):
            temp = arr[i]
            arr[i] =arr[j]
            arr[j] = temp
            
print('elment of aaray sorted in ascending order')
for i in range(0,len(arr)):
    print(arr[i] ,end=' ')
    
###alternate method  
# print(sorted(arr))