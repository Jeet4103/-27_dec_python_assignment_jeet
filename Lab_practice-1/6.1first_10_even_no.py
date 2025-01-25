def generate_even_numbers():
    for num in range(2, 21, 2):
        yield num

# Using the generator
for even in generate_even_numbers():
    print(even)
