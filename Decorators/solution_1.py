# Problem 1

import time

def executionTime(fx):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fx(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f'{fx.__name__} executed in {execution_time}')
        return result
    return wrapper



@executionTime
def greeting(name, greet):
    time.sleep(3)
    print(f'Hello {name}, {greet}')

greeting('Arpan', 'hi')