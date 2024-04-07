import array
arr = array.array('i',[1,2,3,1,2,5])
print('the new created array is:' , end=" ")
for i in range(0,6):
    print(arr[i], end=" ")
print('\r')
print(' the index of 1st occurrence of 2 is :' ,end = "")
print(arr.index(2))
print('the index of 1st occurence of 1 is:' ,end =" ")
print(arr.index(1))