data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 118, 191, 350, 360]

# edge cases and corner cases 

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#        160, 170, 183, 185, 187, 118, 191]

# data = [104, 105, 110, 120, 130, 130, 150,
#        160, 170, 183, 185, 187, 118, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150,
#        160, 170, 183, 185, 187, 118, 191]

# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]

# data = []

min_value = 100
max_value = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_value:
        stop = index
        break

print(stop) # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_value:
        # We have the index of the last item to keep
        # Set "start" to the position of the first
        # item to delete, which is 1 after "index".
        start = index + 1
        break

print(start) # for debugging
del data[start:]
print(data)