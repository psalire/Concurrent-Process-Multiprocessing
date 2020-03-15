# Python Multiprocessing class

Class for creating concurrent processes for multiprocessing in Python

## How it works

The spawned process consumes data from a queue.

If the queue is empty, wait for data. Else, once data is pushed to the queue, pop the queue and call the intended function on it.

## How to use

### General usage

```
from concurrent_process import Concurrent_Process

# Functions
def ftn_1(val):
    # Do something
def ftn_2(val):
    # Do something

# Create 2 processes
proc_1 = Concurrent_Process(ftn_1, 'PROC_1')
proc_2 = Concurrent_Process(ftn_2, 'PROC_2')

# Start processes
proc_1.start()
proc_2.start()

# Push data to queue that processes will process using ftn_x
proc_1.push_to_queue(data_1)
proc_2.push_to_queue(data_2)
```

### Example usage

See ```main_test.py``` for example usage.
