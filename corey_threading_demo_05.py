# We will use ThreadPoolExecutor
import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s).')
    time.sleep(seconds)
    return 'Done sleeping.'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1) #returns a future object
    f2 = executor.submit(do_something, 1) #returns a future object

    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')