import random
import time

def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Randomly select a pivot
    pivot = random.choice(arr)

    # Partition the array into three parts
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Determine where the k^th element lies
    if k < len(low):
        return randomized_select(low, k)
    elif k < len(low) + len(pivots):
        return pivots[0]
    else:
        return randomized_select(high, k - len(low) - len(pivots))


# Function to test the algorithm with timing
def test_randomized_select():
    test_cases = [
        # Edge Case 1: Small array
        ([3, 1, 2, 4, 5], 2, "Small Array"),
        # Edge Case 2: Large array with duplicates
        ([random.randint(1, 100) for _ in range(1000)], 500, "Large Array with Duplicates"),
        # Edge Case 3: Reverse-sorted array
        (list(range(1000, 0, -1)), 200, "Reverse-Sorted Array"),
    ]

    for array, k, description in test_cases:
        start_time = time.time()
        result = randomized_select(array, k - 1)  # k - 1 for 0-based indexing
        end_time = time.time()
        print(f"Test Case: {description}")
        print(f"The {k}th smallest element is: {result}")
        print(f"Time taken: {end_time - start_time:.6f} seconds\n")


if __name__ == "__main__":
    test_randomized_select()
