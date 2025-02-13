import random

random_integer = random.randint(1, 100)
print(f"Random Integer: {random_integer}")

print()
random_float = random.random()
print(f"Random Float: {random_float}")

print()
random_uniform = random.uniform(1.5, 10.5)
print(f"Random Uniform Float: {random_uniform}")

print()
sample_list = [10, 20, 30, 40, 50]
random_choice = random.choice(sample_list)
print(f"Random Choice from List: {random_choice}")

print()
random.shuffle(sample_list)
print(f"Shuffled List: {sample_list}")

print()
random_sample = random.sample(sample_list, 3)
print(f"Random Sample from List: {random_sample}")