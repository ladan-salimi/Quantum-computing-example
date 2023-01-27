from dimod import ConstrainedQuadraticModel, Integer
from dimod import ExactCQMSolver
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
sampleset = ExactCQMSolver().sample_cqm(cqm)
print(sampleset)   
#SampleSet.filter:Return a new sampleset with rows filtered by the given predicate.
#the first arument of SampleSet.filter must be a A function that accepts a named tuple as returned by data() and returns a bool.
#So we use lambda function that is a small anonymous function with syntax of:
#lambda arguments : expression that The expression is executed and the result is returned:
#A lambda function can take any number of arguments, but can only have one expression.
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  
if len(feasible_sampleset): 
#Sample with the lowest-energy:     
   best = feasible_sampleset.first
   print(best)
   #%%
stop = timeit.default_timer()
#stop time
general=stop - start
print('Time: ', general) 