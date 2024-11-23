class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            raise IndexError("Index out of bounds")

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        else:
            raise IndexError("Index out of bounds")

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        return self.data


class Matrix:
    def __init__(self, rows, cols):
        self.data = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            self.data[row][col] = value
        else:
            raise IndexError("Index out of bounds")

    def access(self, row, col):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            return self.data[row][col]
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        return self.data


# Example usage
if __name__ == "__main__":
    # Array Operations
    array = Array()
    array.insert(0, 10)  # Insert at index 0
    array.insert(1, 20)  # Insert at index 1
    array.insert(1, 15)  # Insert at index 1
    print("Array after insertions:", array.display())
    print("Access element at index 1:", array.access(1))
    print("Deleted element at index 0:", array.delete(0))
    print("Array after deletion:", array.display())

    # Matrix Operations
    matrix = Matrix(3, 3)
    matrix.insert(1, 1, 5)  # Insert value 5 at position (1, 1)
    matrix.insert(0, 2, 10)  # Insert value 10 at position (0, 2)
    print("Matrix after insertions:")
    for row in matrix.display():
        print(row)
    print("Access element at position (1, 1):", matrix.access(1, 1))
