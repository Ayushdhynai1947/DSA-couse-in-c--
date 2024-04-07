my_aaray = []

# Input number of elements
num_elements = int(input('Enter the number of elements in the array: '))

# Loop to input elements
for k in range(num_elements):
    element = input("Enter the element {}: ".format(k+1))
    my_aaray.append(element)
    
print("Array:", my_aaray)

# Input value to remove
val = input("Enter the value to remove: ")

# Check if value exists in array and remove it
if val in my_aaray:
    my_aaray.remove(val)
    print("Array after removal:", end=" ")
    for i in range(len(my_aaray)):
        print(my_aaray[i], end=" ")
else:
    print('Value not found in array')
  