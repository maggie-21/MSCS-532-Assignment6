import time
from Arrays_and_Matrics import Array, Matrix
from Stack_and_queue import Stack, Queue
from Rooted_Tree import TreeNode


# Performance Measurement
def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


if __name__ == "__main__":
    # Initialize Data Structures
    task_array = Array()
    task_matrix = Matrix(100,100)  # Adjacency matrix for dependencies
    undo_stack = Stack()
    task_queue = Queue()
    root_task = TreeNode("Root")

    # Generate Random Tasks
    tasks = [f"Task-{i}" for i in range(1000)]

    # Arrays: Add and Remove Tasks
    _, time_array_add = measure_time(task_array.insert, 0, tasks[0])
    _, time_array_delete = measure_time(task_array.delete, 0)

    # Matrices: Add and Remove Dependencies
    _, time_matrix_add = measure_time(task_matrix.insert, 1, 2, 1)
    _, time_matrix_remove = measure_time(task_matrix.insert, 1, 2, 0)

    # Stacks: Push and Pop Undo Operations
    _, time_stack_push = measure_time(undo_stack.push, "Undo-Task")
    _, time_stack_pop = measure_time(undo_stack.pop)

    # Queues: Enqueue and Dequeue Tasks
    _, time_queue_enqueue = measure_time(task_queue.enqueue, tasks[1])
    _, time_queue_dequeue = measure_time(task_queue.dequeue)

    # Trees: Add Subtasks
    child_task = TreeNode("Subtask")
    _, time_tree_add = measure_time(root_task.add_child, child_task)

    # Output Performance Results
    print(f"Array Add Task Time: {time_array_add:.6f} seconds")
    print(f"Array Delete Task Time: {time_array_delete:.6f} seconds")
    print(f"Matrix Add Dependency Time: {time_matrix_add:.6f} seconds")
    print(f"Matrix Remove Dependency Time: {time_matrix_remove:.6f} seconds")
    print(f"Stack Push Time: {time_stack_push:.6f} seconds")
    print(f"Stack Pop Time: {time_stack_pop:.6f} seconds")
    print(f"Queue Enqueue Time: {time_queue_enqueue:.6f} seconds")
    print(f"Queue Dequeue Time: {time_queue_dequeue:.6f} seconds")
    print(f"Tree Add Subtask Time: {time_tree_add:.6f} seconds")
