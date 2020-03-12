# Python Multiprocessing / Concurrent Process class

Class for creating a concurrent process in Python

## General usage

```
from concurrent_process import Concurrent_Process

# Create 2 processes
proc_1 = Concurrent_Process(ftn_1, 'PROC_1')
proc_2 = Concurrent_Process(ftn_2, 'PROC_2')

# Start processes
proc_1.start()
proc_2.start()

# Push data for processes to use with ftn_x
sleep_proc_1.push_to_queue(data_1)
sleep_proc_2.push_to_queue(data_2)
```

## Example usage

See ```main_test.py``` for example usage.
