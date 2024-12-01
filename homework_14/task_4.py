def chunk_data(data, chunk_size):
    return tuple(tuple(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 2

print("Data:", data)
print("Chunk size:", chunk_size)

print("Chunked data:")
for i in chunk_data(data, chunk_size):
    print(i)