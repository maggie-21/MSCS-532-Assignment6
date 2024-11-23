# Medians and Order Statistics & Elementary Data Structures

This repository contains the implementation and analysis of **selection algorithms** and **elementary data structures** as part of an assignment. The project explores the theoretical and practical aspects of these foundational concepts.

## **Project Structure**

### **Part 1: Medians and Order Statistics**
- **Objective**: Implement and analyze algorithms to find the k^th smallest element in an array.
- **Algorithms Implemented**:
  1. **Deterministic Selection Algorithm (Median of Medians)**:
     - Guarantees O(n) worst-case time complexity.
  2. **Randomized Selection Algorithm (Quickselect)**:
     - Achieves O(n) expected time complexity.
- **Files**:
  - `Deterministic_Algorithm_Median_of_Medians.py`
  - `Randomized_QuickSelect.py`
- **Edge Cases Tested**:
  - Small arrays, arrays with duplicates, and reverse-sorted arrays.
- **Performance Analysis**:
  - Deterministic algorithm is robust and consistent.
  - Randomized algorithm is faster in average cases.

### **Part 2: Elementary Data Structures**
- **Objective**: Implement and analyze arrays, matrices, stacks, queues, linked lists, and rooted trees.
- **Data Structures Implemented**:
  1. **Array**: Manage task lists with operations like insertion, deletion, and access.
  2. **Matrix**: Represent task dependencies using an adjacency matrix.
  3. **Stack**: Handle undo operations (LIFO).
  4. **Queue**: Process tasks in FIFO order.
  5. **Singly Linked List**: Perform dynamic operations like insertion, deletion, and traversal.
  6. **Rooted Tree**: Represent hierarchical tasks with subtasks.
- **Files**:
  - `Arrays_and_Matrics.py`
  - `Stack_and_Queue.py`
  - `Single_LinkedList.py`
  - `Rooted_Tree.py`

---

## **Task Scheduler App**

### **Objective**
A simple task scheduler app simulates real-world usage of arrays, matrices, stacks, queues, and rooted trees. The app:
- **Arrays**: Manages task lists.
- **Matrices**: Represents dependencies between tasks.
- **Stacks**: Tracks undo operations.
- **Queues**: Handles FIFO task processing.
- **Rooted Trees**: Represents hierarchical task groups.

### **File**
- `App.py`

### **Performance Results**
| **Operation**                | **Time Taken (seconds)** |
|------------------------------|--------------------------|
| **Array Add Task**           | 0.000002                |
| **Array Delete Task**        | 0.000001                |
| **Matrix Add Dependency**    | 0.000001                |
| **Matrix Remove Dependency** | 0.000001                |
| **Stack Push**               | 0.000000                |
| **Stack Pop**                | 0.000001                |
| **Queue Enqueue**            | 0.000001                |
| **Queue Dequeue**            | 0.000001                |
| **Tree Add Subtask**         | 0.000000                |

---

## **Usage**

1. **Clone the Repository**:
   ```bash
   git git@github.com:maggie-21/MSCS-532-Assignment6.git
   cd MSCS-532-Assignment6
2. **Run the Algorithms**:

Deterministic Selection:
  ```bash
  python3 Deterministic_Algorithm_Median_of_Medians.py
  ```
Randomized Selection:
  ```bash
  python3 Randomized_QuickSelect.py
  ```
**Test Data Structures**:

Arrays and Matrices:
  ```bash
  python3 Arrays_and_Matrics.py
```
Stacks and Queues:
  ```bash
  python3 Stack_and_Queue.py
```
Singly Linked List:
  ```bash
python3 Single_LinkedList.py
```
Rooted Tree:
  ```bash
  python3 Rooted_Tree.py
```
Run the Task Scheduler App:
  ```bash
    python3 App.py

