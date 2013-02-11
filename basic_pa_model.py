### ----------------------- A PRINCIPAL AGENT MODEL IN PYTHON. ----------------------- ###
### These models build upon the MIT course 15.903 "Organizational economics and        ###
###                    corporate strategy" taught by Robert Gibbons                    ###
### ---------------------------------------------------------------------------------- ###

# ---------------------------------- The basic model. ---------------------------------- #

import sympy as SP
import matplotlib.pyplot as plt
from sympy.solvers import solve
import numpy

class Principal:
	def __init__(self, outcome):
		self.parameter_1 = SP.Symbol(outcome)
	
	def parameters(self):
		return self.parameter_1
	
	def profit_function(self, wage):
		return self.parameter_1 - wage
	
class Agent:
	def __init__(self, action, noise):
		self.parameter_1 = SP.Symbol(action)
		self.parameter_2 = SP.Symbol(noise)

	def parameters(self):
		return self.parameter_1, self.parameter_2

	def cost_function(self, pm1, pm2):
		return pm1*(self.parameter_1**pm2)

class Contract:
	def __init__(self, base_pay, commission):
		self.parameter_1 = SP.Symbol(base_pay)
		self.parameter_2 = SP.Symbol(commission)
	
	def parameters(self):
		return self.parameter_1, self.parameter_2

if __name__ == "__main__":
# in the course notes:
# y => outcome
# a => action
# e => noise factor
# s => base pay
# b => commission/bonus pay

	# create objects.
	principal = Principal("y")
	agent = Agent("a", "e")
	contract = Contract("s", "b")
	
	# get parameters and equations
	a, e = agent.parameters()
	s, b = contract.parameters()
# Can we get rid of the principal class?
	y = principal.parameters()
	y = a + e
	wage = s + b*y
	
	cf = agent.cost_function(0.5, 2)
	pf = principal.profit_function(wage)

	# solve the maximisation problem for the agent.
	policy_function = wage - cf
	solution = solve(policy_function, a)

	# set parameter values in the profit function
	# possible to add a noise term here and rerun monte carlo simulations.
#	pf = pf.subs("y", 1)
#	pf = pf.subs("e", 0)
#	pf = pf.subs("s", 0.15)
#	pf = pf.subs("b", 0.15)
#	wage = wage.subs("e", 0)
#	wage = wage.subs("s", 0.15)
#	wage = wage.subs("b", 0.15)

	# plot the profit and cost function
#	axis = numpy.arange(0,1,0.001)
#	cf_graph = [cf.subs('a', number) for number in axis]
#	pf_graph = [pf.subs('a', number) for number in axis]
#	wage_graph = [wage.subs('a', number) for number in axis]
#	plt.plot(axis, cf_graph, 'r', label = 'Cost function')
#	plt.hold(True)
#	plt.plot(axis, pf_graph, 'b', label = 'Profit function')
#	plt.plot(axis, wage_graph, 'g', label = 'Wage function')
#	plt.legend(loc = 0)
#	plt.title('Profit and Cost function')
#	plt.show()