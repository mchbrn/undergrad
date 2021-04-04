x = 10
y = 5

coordinates = []

for row in range(x):
    print(row)
    coordinates.append([])
    for column in range(y):
        coordinates[row].append([])

cellx, celly = 0, 0
coordinates[0][1] = "hello"
coordinates[cellx + 5][celly + 1] = "goodbye"
print(coordinates)
