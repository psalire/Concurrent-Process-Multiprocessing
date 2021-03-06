from concurrent_process import Concurrent_Process
from time import sleep
from random import uniform
import signal, sys, os

# Catch CTRL-C
def keyboard_interrupt(signal, frame):
    print('Keyboard interrupt. Exiting...')
    sys.exit(0)

def sleep_time(time, name):
    print('[{}] Sleeping for {} s...'.format(name, time))
    sleep(time)
    print('[{}] Sleeping done'.format(name))

def main():
    # Catch CTRL-C
    signal.signal(signal.SIGINT, keyboard_interrupt)
    
    # Create 2 processes
    proc_1 = Concurrent_Process(sleep_time, 'PROC_1')
    proc_2 = Concurrent_Process(sleep_time, 'PROC_2')
    # Start processes
    proc_1.start()
    proc_2.start()    
    
    # Push 10 elements to each queue
    for _ in range(10):
        # Do processing (sleep) for 1-10 seconds in each process
        rand_1, rand_2 = uniform(1,10), uniform(1,10)
        proc_1.push_to_queue(rand_1)
        proc_2.push_to_queue(rand_2)
        print('[MAIN] Pushed to PROC_1 queue: {}'.format(rand_1))
        print('[MAIN] Pushed to PROC_2 queue: {}'.format(rand_2))
        # Wait 3 seconds before pushing more to queue
        sleep(3)
    print('No more elements being added.')
    # Wait for queues to empty, then exit
    proc_1.stop()
    proc_2.stop()

if __name__ == '__main__':
    main()
