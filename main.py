from pso import PSO
from functions import *

# Originally developed by Nathan A. Rooy in July, 2016

initial = [5, 5]  # initial starting location [x1,x2...]
bounds = [(-10, 10), (-10, 10)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
PSO(sphere, initial, bounds, num_particles=100, maxiter=100)
PSO(rastrigin, initial, bounds, num_particles=100, maxiter=100)
PSO(rosenbrock, initial, bounds, num_particles=100, maxiter=100)
