from multiprocessing import Process
from typing import Union
import concurrent.futures
import os
from functools import wraps


class NotParallelizable(Exception):
    pass


def as_parallel(func):
    """
    Decorator that allows a function to be parallelized.

    Pass a list after the function name to be parallelized containing the inputs
    for the function in question. If desired, keyword arguments can also be passed
    seperately for a small and usually insignificant performance reduction.
    """

    @wraps(func)
    def wrapper(lst: list):
        num_threads_mult = 2
        num_workers = int(os.cpu_count()*num_threads_mult)
        if len(lst) < num_workers:
            num_workers = len(lst)
        
        if num_workers:
            if num_workers == 1:
                result = [func[lst[0]]]
            else:
                result = []
                with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as execute:
                    bag = {execute.submit(func, i): i for i in lst}
                    for future in concurrent.futures.as_completed(bag):
                        result.append(future.result())
        else:
            result = []
        
        return result
    return wrapper
    
    
def run_parallel(*functions, get_returns=True) -> Union[None, dict]:
    """
    Wrapper function to run specified functions in parallel.
    
    Takes arbitrary amount of functions as arguments, as well as a boolean representing
    whether to get return values for these statements.

    If get_returns is set to True, function will return a dictionary where
    keys represent the function passed and values represent the returns of those
    functions.
    """
    for i in functions:
        if not callable(i):
            raise NotParallelizable(f"Object {i} does not carry <type 'function'>.")
    
    processes = []
    for function in functions:
        proc = Process(target=function)
        proc.start()
        processes.append(proc)
    
    for proc in processes:
        proc.join()
