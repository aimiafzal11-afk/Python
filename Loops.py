#for loop
for i in range(3):
    print(("Hello World!"))

for i in range(5, 0, -1):
    print(i)
for char in "hello":
    print(char)

#while loop
count = 1
while count<= 5:
    print(count)
    count += 1

#nested loop
for i in range(2):
    print("Outer loop")
    for j in range(2):
        print("  Inner loop")

#4*4 matrix
i = 4
rows = i
cols = i
matrix = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(0)
    matrix.append(rows)
for rows in matrix:
    print(' '.join(map(str, row)))