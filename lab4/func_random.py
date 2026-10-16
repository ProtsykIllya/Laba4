import random
def random_numbers(count, low, high):
    return [random.randint(low, high) for _ in range(count)]