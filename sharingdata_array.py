import multiprocessing

def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n
        
if __name__ == "__main__":        
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    process = multiprocessing.Process(target = calc_square, args = (numbers, result ))
    process.start()
    process.join()

    print(result[:])