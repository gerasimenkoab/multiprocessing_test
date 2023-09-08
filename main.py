import os
import time
import random
from multiprocessing import Pool
import tkinter as tk

class multiprocessingTestManyArgsClass(object):
    '''Class with many argument function which should be executed. '''
    def __init__(self):
        print('Many Args Test Initialized:')
        print(" - Number of cpu cores %d" %os.cpu_count())
        self.pool_size = 3
        print(' - Workers pool size set to %d'%self.pool_size)
        self.result = None

    def funcManyArgs(self, a, b):
        sleepTime = random.randint(0,9)
        result = a + b
        print('Process id: %d , Sleep time: %d' %(os.getpid(), sleepTime))
        time.sleep(sleepTime)
        return result

    def run_pool(self):
        '''Running worker funcion in parallel'''
        arg1 = [1,2,3]
        arg2 = [3,4,5]
        with Pool(processes = self.pool_size) as p:
            self.result = p.starmap(self.funcManyArgs, zip(arg1, arg2)) #[(2,3),(4,5),(6,7)])
            #result = pool.starmap(funcManyArgs, zip(a_args, repeat(second_arg)))
            #result = pool.map(partial(funcManyArgs, b=second_arg), a_args) # old versions
        print('Test with many args done.')

    def print_result(self):
        print('Many args result:', self.result)

class multiprocessingTestSingleArgClass(object):
    '''Class with single argument function which should be executed. '''
    def __init__(self):
        print('- One Arg Test Initialized:')
        print(' - Number of cpu cores: %d' % os.cpu_count())
        self.result = None
        self.pool_size = 4
        print(" - Workers pool size set to %d" %self.pool_size)

    def f_worker(self, x):
        '''This function execute in parallel in pool of workers'''
        sleepTime = random.randint(0, 9)
        print('Process id: %d , Sleep time: %d' %(os.getpid(), sleepTime))
        time.sleep(sleepTime)
        return x * x
    
    def run_pool(self):
        '''Run pool of processes and recieve result'''
        with Pool(self.pool_size) as p:
            self.result =  p.map(self.f_worker,[1,5,3,6,9])
        print("Test with one arg done.")

    def print_result(self):
        print("One arg result:", self.result)


if __name__ == '__main__':
    root = tk.Tk()
    a = multiprocessingTestSingleArgClass() # create class with one arg function
    b = multiprocessingTestManyArgsClass() # create class with many args function
    tk.Button(root, text = 'One arg test', width = 15, pady = 10, command= lambda: a.run_pool()).pack(side = 'top', pady = 10, padx=5)
    tk.Button(root, text = 'Many args test', width = 15, pady = 10, command = lambda: b.run_pool()).pack(side = 'top', pady = 10, padx=5)
    tk.Button(root, text = 'Print one arg', width = 15, pady = 10, command= lambda: a.print_result()).pack(side = 'top', pady = 10, padx=5)
    tk.Button(root, text = 'Print many args', width = 15, pady = 10, command= lambda: b.print_result()).pack(side = 'top', pady = 10, padx=5)
    root.mainloop()
