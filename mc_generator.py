import numpy as np
import matplotlib.pyplot as plt

from numpy.random import normal
from numpy.random import uniform
from numpy.random import exponential
from numpy.random import noncentral_chisquare

def _time_change(t):
    return t

'''
class MarkovProcess(trans, time_change, initial_state)
    Used to generate a real-value Markov Process given transition probability

Method:
.get_simulation(num_trails = 1000, start_time = 0, end_time = 1)
    Input: 
        num_trails - a positive integer. number of points
        start_time - a positive real number.
        end_time - a positive real number.
    Output:
        np.array with dim = (num_trails, 2). Each row represent a point (t, B_t).
''' 
class MarkovProcess:
    def __init__(self, trans, time_change=_time_change, initial_state=0):
        self.initial_state = initial_state
        self.trans = trans 
        self.time_change = time_change
        
    def simulate(self, num_trails=1000, start_time=0.0, end_time=1.0):
        self._num_trails = num_trails
        self._start_time = start_time
        self._end_time = end_time
        
        time_change = self.time_change
        current_state = self.initial_state
        current_time = start_time
        increment = (end_time-start_time)/num_trails
        time_list = [current_time]
        state_list = [current_state]
        
        get_new_state = self.trans
        
        for i in range(num_trails): 
            current_state = get_new_state( time_change(current_time), current_state, time_change(current_time + increment) )
            current_time += increment 
            time_list.append(current_time)
            state_list.append(current_state)
        
        self.time = time_list
        self.simulation = state_list
        
    def get_simulation(self):
        self.simulate(self._num_trails, self._start_time, self._end_time)
        return [self.time, self.simulation]
        
    def figure(self):
        output = self.get_simulation()
        plt.plot(output[0],output[1])
        
class BrownianMotion(MarkovProcess):
    def __init__(self, initial_state=0):
        def BM_trans( current_time, current_state, next_time ):
            return normal()*np.sqrt( next_time - current_time ) + current_state
        self.initial_state = initial_state
        self.trans = BM_trans 
        self.time_change = _time_change
        
class CIR(MarkovProcess):
    def __init__(self, a=1.0, b=1.2, sigma=0.2, initial_state=0):
        def CIR_trans( ctime, cstate, ntime ):
            dt = ntime - ctime
            r_t = cstate
            c = 2*a/(  (1 - np.exp(-a*dt))*(sigma**2) )
            degree_of_freedom = 4*a*b/sigma**2
            non_centrality = 2 * c * r_t * np.exp(-a * dt)  
            return noncentral_chisquare(degree_of_freedom, non_centrality)/(2*c)
        
        self.initial_state = initial_state
        self.trans = CIR_trans 
        self.time_change = _time_change
        
class Poission(MarkovProcess):
    def __init__(self, beta = 1.0, time_change=_time_change, initial_state=0):
        #NOTE: beta:= 1/ lemabda
        def Poission_trans( current_time, current_state, next_time ):
            dt = next_time - current_time
            next_jump_time = exponential(beta)
            if next_jump_time<= dt:
                return current_state+1
            else:
                return current_state
        self.initial_state = initial_state
        self.trans = Poission_trans
        self.time_change = time_change
        
class CoutingProcess(MarkovProcess):
    def __init__(self, intensity, initial_state=0): 
        beta = 1
        def Poission_trans( current_time, current_state, next_time ):
            dt = next_time - current_time
            next_jump_time = exponential(beta)
            if next_jump_time<= dt:
                return current_state+1
            else:
                return current_state
        
        self.initial_state = initial_state
        self.trans = Poission_trans 
        self.intensity = intensity
    
    def simulate(self, num_trails=1000, start_time=0.0, end_time=1.0):
        self._num_trails = num_trails
        self._start_time = start_time
        self._end_time = end_time
         
        current_state = self.initial_state
        current_time = start_time
        increment = (end_time-start_time)/num_trails
        time_list = [current_time]
        state_list = [current_state]
        intensity = self.intensity
        
        get_new_state = self.trans
        
        changed_current_time = 0
        for i in range(num_trails): 
            if i != 0:
                changed_current_time += increment * intensity[i-1]
                changed_next_time = changed_current_time + increment * intensity[i]
                
                current_state = get_new_state( changed_current_time, current_state, changed_next_time )
                current_time += increment 
                time_list.append(current_time)
                state_list.append(current_state)
        
        self.time = time_list
        self.simulation = state_list