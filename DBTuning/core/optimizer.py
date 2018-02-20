import GPyOpt
import numpy as np

from datetime import datetime


class Optimizer(object):

    def __init__(self, db):
        self.db = db


    def _get_random_values(self):
        v = [np.random.uniform(low=param['domain'][0], high=param['domain'][1]) for param in self.db.domain]
        return np.array(v)

    

    def run_optimization(self):
    
        values = self._get_random_values()
        self.db.set_params_vector(values)
        target = self.db.collect_metric()

        X = np.array([values])
        Y = np.array([[target]])
        
        values = self._get_random_values()
        self.db.set_params_vector(values)
        target = self.db.collect_metric()

        X = np.r_[X,[values]]
        Y = np.r_[Y, [[target]]]

        for i in range(5000):

            a = datetime.now()

            bo_step = GPyOpt.methods.BayesianOptimization(f = None, domain = self.db.domain, X = X, Y = Y, model_type='sparseGP')
            if i%100 == 0:
                x_next = bo_step.suggest_next_locations()
            else:
                x_next = np.array([self._get_random_values()])
            self.db.set_params_vector(x_next[0])
            target = self.db.collect_metric()

            b = datetime.now()
            
            
            X = np.r_[X, x_next]
            Y = np.r_[Y, [[target]]]

            if i%100 == 0:         
                print (X.shape)
                print (Y.shape)
                print (x_next)
                print (target)
                print (b-a)


        exit(0)

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
