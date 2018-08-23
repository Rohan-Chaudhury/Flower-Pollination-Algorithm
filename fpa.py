from NiaPy.algorithms.basic import FlowerPollinationAlgorithm
import numpy as np
import cmath
import math
# our custom benchmark classs
class MyBenchmark(object):
    def __init__(self):
        # define lower bound of benchmark function
        self.Lower = 0.0001
        # define upper bound of benchmark function
        self.Upper = 1000

    # function which returns evaluate function
    def function(self):
        def evaluate(D, sol):
            u=np.arange(0.01,100,(100-0.01)/100)
            #u=(0.01,10**5,10)
            
            val = 0.0
            for i in u:
                a=i*1j
                val=val + abs(( a**0.82 - (a**3*sol[0]+a**2*sol[1]+a**1*sol[2]+a**0*sol[3])/(a**3*sol[4]+a**2*sol[5]+a**1*sol[6]+a**0*sol[7]+1))**2)

            print(val)   
            return val
            
            
        return evaluate



for i in range(10):
    print('Process started')
    algorithm = FlowerPollinationAlgorithm(8, 50,80000,0.85, MyBenchmark())
    best = algorithm.run()
    print('The dimension values are:')
    for i in range(8):
        print(algorithm.best[i])

    print('the error is:')
    print(20*math.log10(best))
    
    

