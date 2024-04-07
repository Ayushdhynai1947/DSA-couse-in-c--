# entering element in an array
my_array = []

# Ask the user for input
n = int(input("Enter the number of elements: "))

# Loop to enter elements
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    my_array.append(element)

# Print the array
print("Array:", my_array)
