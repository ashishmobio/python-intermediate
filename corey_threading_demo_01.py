# Python Threading Tutorial: Run Code Concurrently Using the Threading Module
# https://www.youtube.com/watch?v=IEEhzQoKtQU
# Corey Schafer

import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second.')
    time.sleep(1)
    print('Done sleeping.')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Synchronous Running (in order)
# https://drive.google.com/file/d/1HSRGy8mgTbaEmS25nSXizNEl3TLoxG0c/view?usp=sharing

# CPU bound tasks are the ones that crunch lot of numbers and using CPU.
# IO bound tasks are the ones that waiting for IO operations to be completed and not really using CPU that much. 
# Examples of IO bound tasks: reading and writing from the file system, network operations, downloading stuff online etc.

# Threading is really useful for IO bound tasks.
# That is tasks are waiting around IO operations.

# Multi-processing is really useful for CPU bound tasks.
# That is for the tasks involved data crunching.

# Threading gives an illusion of parallel running but in reality is concurrency.
# https://drive.google.com/file/d/15k0PaKscuRkr0RutKWBLl7SKYr5E_DTU/view?usp=sharing





