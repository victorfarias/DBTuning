import GPyOpt

class Optimizer(object):

    def __init__(self, db):
        self.db = db

    def run_optimization(self):

        bo_step = GPyOpt.methods.BayesianOptimization(f = None, domain = self.db.domain, X = np.array([[]]), Y = np.array([]))
        x_next = bo_step.suggest_next_locations()
        
                
        # X_init = np.array([[0.0],[0.5],[1.0]])
        # Y_init = func.f(X_init)

        # iter_count = 10
        # current_iter = 0
        # X_step = np.array([])
        # Y_step = np.array([])

        # while current_iter < iter_count:
        #     bo_step = GPyOpt.methods.BayesianOptimization(f = None, domain = domain, X = X_step, Y = Y_step)
        #     x_next = bo_step.suggest_next_locations()
        #     y_next = func.f(x_next)
            
        #     X_step = np.vstack((X_step, x_next))
        #     Y_step = np.vstack((Y_step, y_next))
            
        #     current_iter += 1
