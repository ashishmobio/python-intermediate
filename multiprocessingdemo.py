import time
import multiprocessing

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
        
if __name__ == "__main__":        
    arr = [2, 3, 8, 9]

    # Target can be thought as task to be performed.
    process1 = multiprocessing.Process(target = calc_square, args = (arr, ))
    process2 = multiprocessing.Process(target = calc_cube, args = (arr, ))

    ## Start the process 1 and 2 in parallel.
    process1.start()
    process2.start()

    ## Process 1 (squaring) and Process 2 (cubing) are done and joined backs to main Process.
    process1.join()
    process2.join()

    print("Done with squaring and cubing.")