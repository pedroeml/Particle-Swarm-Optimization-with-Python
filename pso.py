from particle import Particle


class PSO:
    def __init__(self, cost_func, x0, bounds, num_particles, maxiter):
        self.cost_func = cost_func
        self.x0 = x0
        self.bounds = bounds
        self.num_particles = num_particles
        self.maxiter = maxiter

        self.num_dimensions = len(x0)
        self.err_best_g = -1  # best error for group
        self.pos_best_g = []  # best position for group
        self.swarm = []

        self.establish_swarm()
        self.optimization()
        self.results()

    def establish_swarm(self):
        """
        Establish the swarm.

        :return:
        """
        for i in range(0, self.num_particles):
            self.swarm.append(Particle(self.x0, self.num_dimensions))

    def optimization(self):
        """
        Begin optimization loop.

        :return:
        """
        i = 0
        while i < self.maxiter:
            # print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, self.num_particles):
                self.swarm[j].evaluate(self.cost_func)

                # determine if current particle is the best (globally)
                if self.swarm[j].err_i < self.err_best_g or self.err_best_g == -1:
                    self.pos_best_g = list(self.swarm[j].position_i)
                    self.err_best_g = float(self.swarm[j].err_i)

            # cycle through swarm and update velocities and position
            for j in range(0, self.num_particles):
                self.swarm[j].update_velocity(self.pos_best_g)
                self.swarm[j].update_position(self.bounds)
            i += 1

    def results(self):
        """
        Print final results.

        :return:
        """

        print('Function: ' + self.cost_func.__name__ +
              '\nBest position: ' + str(self.pos_best_g) +
              '\nFunction solution: ' + str(self.err_best_g) +
              '\n')
