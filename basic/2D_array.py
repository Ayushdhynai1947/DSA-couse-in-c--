# enter element in 2D aaray


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
array_2d = []

# Input elements into the 2D array
for i in range(rows):
    row = []
    for j in range(cols):
        element = input("Enter element at position ({}, {}): ".format(i, j))
        row.append(element)
    array_2d.append(row)

# Print the 2D array
print("2D Array:")
for row in array_2d:
    print(row)
    