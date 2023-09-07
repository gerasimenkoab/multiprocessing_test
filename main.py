import os
import time
import random
from multiprocessing import Pool
import tkinter as tk


class multiprocessingTestClass(object):
    '''Class with function which should be executed. '''
    def __init__(self):
        print('Number of cpu cores: %d' % os.cpu_count())
        self.result = None
        self.pool_size = 4
        print("Workers pool size set to %d" %self.pool_size)
    def f_worker(self, x):
        '''This function execute in parallel in pool of workers'''
        sleepTime = random.randint(0, 9)
        print("sleep time:", sleepTime, ' process ID:', os.getpid())
        time.sleep(sleepTime)
        return x * x
    def run_pool(self):
        '''Run pool of processes and recieve result'''
        with Pool(self.pool_size) as p_class:
            self.result =  p_class.map(self.f_worker,[1,5,3,6,9])
        print("Done.")
    def print_result(self):
        print("Result:", self.result)


if __name__ == '__main__':
    root = tk.Tk()
    a = multiprocessingTestClass() # create class with 
    tk.Button(root, text = 'Start', command= lambda: a.run_pool()).pack(side='top')
    tk.Button(root, text = 'Print', command= lambda: a.print_result()).pack(side='top')
    root.mainloop()
