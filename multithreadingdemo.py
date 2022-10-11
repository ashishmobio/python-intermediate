import time
import threading

def calc_square(numbers):
    print("Calculate the square of numbers.")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ", n*n)

def calc_cube(numbers):
    print("Calculate the cube of numbers.")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ", n*n*n)

if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    t = time.time()

    # Target can be thought as task to be performed.
    thread1 = threading.Thread(target = calc_square, args = (arr, ))
    thread2 = threading.Thread(target = calc_cube, args = (arr, ))

    ## Start the threads 1 and 2 in parallel.
    thread1.start()
    thread2.start()

    ## Threads 1 (squaring) and 2 (cubing) are done and joined backs to main thread.
    thread1.join()
    thread2.join()

    print("Time taken: ", time.time() - t)
    print("Done with squaring and cubing.")