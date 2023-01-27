from dimod import ConstrainedQuadraticModel, Integer
from dwave.system import LeapHybridCQMSampler
import timeit
#%%
start = timeit.default_timer()
#Construct a problem: Of and Constraints:
x= Integer('x',upper_bound=4)
y=Integer('y',upper_bound=4)
cqm = ConstrainedQuadraticModel()
cqm.set_objective(-x*y)
cqm.add_constraint(2*x+2*y<= 8, "Max perimeter")

#%%Solver
sampler = LeapHybridCQMSampler() 
sampleset = sampler.sample_cqm(cqm)
print(sampleset) 
#print("{} feasible solutions of {}.".format(
      #sampleset.record.is_feasible.sum(), len(sampleset))) 
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  
if len(feasible_sampleset):      
   best = feasible_sampleset.first
print(best)
#%%
stop = timeit.default_timer()
#stop time
general=stop - start
print('Time: ', general) 