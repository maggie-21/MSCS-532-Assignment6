import time

def median_of_medians(arr, k):
    # Helper function to find the median of a group
    def find_median(group):
        group.sort()
        return group[len(group) // 2]

    # Step 1: Divide the array into groups of 5
    if len(arr) <= 5:
        arr.sort()
        return arr[k]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [find_median(group) for group in groups]

    # Step 2: Find the median of the medians
    median_of_medians_pivot = median_of_medians(medians, len(medians) // 2)

    # Step 3: Partition the array around the pivot
    low = [x for x in arr if x < median_of_medians_pivot]
    high = [x for x in arr if x > median_of_medians_pivot]
    pivots = [x for x in arr if x == median_of_medians_pivot]

    # Step 4: Determine where the k^th element lies
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(high, k - len(low) - len(pivots))


# Function to test the algorithm with timing
def test_median_of_medians():
    import random
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
        result = median_of_medians(array, k - 1)  # k - 1 for 0-based indexing
        end_time = time.time()
        print(f"Test Case: {description}")
        print(f"The {k}th smallest element is: {result}")
        print(f"Time taken: {end_time - start_time:.6f} seconds\n")


if __name__ == "__main__":
    test_median_of_medians()
