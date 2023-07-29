#  Context managers
""" 
Is an object that that defines a temporary context for a block of code.
Context managers provide a convenient and reliable way to manage resources, such as files or network connections,
ensuring that they are properly initialized and cleaned up.
"""
# Example: Demonstrate a context manager to open a file and return a context manager instance 
# def open_file(filename):
#     file = open(filename, "r")

#     class FileContextManager:
#         def __enter__(self):
#             return file

#         def __exit__(self, exc_type, exc_value, traceback):
#             file.close()

#     return FileContextManager()

# with open_file("my.txt") as f:
#     content = f.read()
#     print(content) 
    
# Example.2  Demonstrate a context manager using a time series.
# import time

# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         elapsed_time = time.time() - self.start_time
#         print(f"Elapsed time: {elapsed_time} seconds")

# # Example usage
# with Timer() as timer:
#     # Code block to measure execution time
#     time.sleep(3)

# Explanation.
""" 
In this example, we define a Timer class that serves as a context manager.
The __enter__ method records the start time using time.time() and returns the instance of the Timer class.
The __exit__ method calculates the elapsed time by subtracting the start time from the current time and prints the result.
Inside the with block, you can place any code that you want to measure the execution time of.
In this case, we use time.sleep(3) to simulate a code block that takes 3 seconds to execute.
The example demonstrates how the context manager measures the execution time of the code block
and provides the elapsed time once the block is finished.
"""


#  Multithreading and multiprocessing
# Are two approaches in Python for achieving concurrent execution and utilizing multiple CPU cores for improved performance. 
""" 
#  Multithreading
Technique where multiple threads within a single process execute concurrently, sharing the same memory space.
It allows for concurrent execution of multiple tasks.

#  Multiprocessing
Technique where multiple processes are created, each having its own memory space.
It allows for parallel execution of tasks on multiple CPU cores.
"""

# Example on multithreading
# import threading

# def thread_task(name):
#     print(f"Running thread {name}")

# # Create multiple threads
# thread1 = threading.Thread(target=thread_task, args=("T1",))
# thread2 = threading.Thread(target=thread_task, args=("T2",))

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for the threads to complete
# thread1.join()
# thread2.join()

# Example on multiprocessing
# import multiprocessing

# def process_task(name):
#     print(f"Running process {name}")

# if __name__ == '__main__':
#     # Create multiple processes
#     process1 = multiprocessing.Process(target=process_task, args=("P1",))
#     process2 = multiprocessing.Process(target=process_task, args=("P2",))

#     # Start the processes
#     process1.start()
#     process2.start()

#     # Wait for the processes to complete
#     process1.join()
#     process2.join()


#  Example: Combines multithreading and multiprocessing.
# import threading
# import multiprocessing

# def task(name):
#     print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

# # Create multiple threads
# threads = []
# for i in range(4):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()
    
# for t in threads:
#     t.join()


# Assignment. 
#  QN.1  Show a context manager for file handling that automatically opens and closes a file.
# class FileHandle:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()

# with FileHandle('my.txt', 'w') as file:
#     file.write('Hello, world!')


#  QN.2  Show a context manager for managing a database connection.
# import sqlite3

# class DatabaseManager:
#     def __init__(self, db_name):
#         self.db_name = db_name
#         self.connection = None

#     def __enter__(self):
#         self.connection = sqlite3.connect(self.db_name)
#         return self.connection

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.connection:
#             self.connection.close()

# with DatabaseManager('sil.db') as con:
#     print("Using the con")

    
#  QN.3  Show multithreading and multiprocessing that allows us to run the function for different amounts of time.
import time
import threading
import multiprocessing

def worker_thread(name, duration):
    print(f"Thread {name} started")
    time.sleep(duration)
    print(f"Thread {name} completed")

def worker_process(name, duration):
    print(f"Process {name} started")
    time.sleep(duration)
    print(f"Process {name} completed")

if __name__ == '__main__':
    # Multithreading 
    thread1 = threading.Thread(target=worker_thread, args=("T1", 3))
    thread2 = threading.Thread(target=worker_thread, args=("T2", 5))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Multiprocessing 
    process1 = multiprocessing.Process(target=worker_process, args=("P1", 3))
    process2 = multiprocessing.Process(target=worker_process, args=("P2", 5))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
