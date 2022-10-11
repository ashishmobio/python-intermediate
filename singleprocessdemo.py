import time
import multiprocessing


square_result = []
def calc_square(numbers):
    global square_result
    ## Note that a new process creates a copy of square result.
    for n in numbers:
        print("Square: ", n*n)
        square_result.append(n*n)
    print("Result within the Process: ", str(square_result))


## Every process has their own address space (virtual memory).
## Thus program variables are not shared between two processes.
## You need to use interprocess communication (IPC) techniques,
## if you want to share date between two processes.

        
if __name__ == "__main__":        
    arr = [2, 3, 8, 9]

    # Target can be thought as task to be performed.
    process = multiprocessing.Process(target = calc_square, args = (arr, ))

    ## Start the process
    process.start()

    ## Join the process.
    process.join()

    print("Result outside the Process: ", str(square_result))
    print("Done with squaring.")