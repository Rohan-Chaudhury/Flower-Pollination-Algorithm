from NiaPy.algorithms.basic import FlowerPollinationAlgorithm

# we will run 10 repetitions of Grey Wolf Optimizer against Pinter benchmark function
for i in range(20):
    # first parameter takes dimension of problem
    # second parameter is population size
    # third parameter takes the number of function evaluations
    # fourth parameter is benchmark function
    algorithm = FlowerPollinationAlgorithm(10, 20 , 10000,0.5, 'pinter')

    # running algorithm returns best found minimum
    best = algorithm.run()

    # printing best minimum
    print(best)
