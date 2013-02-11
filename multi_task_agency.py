### ----------------------- A PRINCIPAL AGENT MODEL IN PYTHON. ----------------------- ###
### These models build upon the MIT course 15.903 "Organizational economics and        ###
###               corporate strategy" taught by Professor Robert Gibbons               ###
### ---------------------------------------------------------------------------------- ###

# ---------------------------- The multi-task agency model. ---------------------------- #

import sympy as SP
#import matplotlib.pyplot as plt
from sympy.solvers import solve
from datetime import datetime

startTime = datetime.now()

class Principal:
	def __init__(self, pm_1, pm_2, pm_3, pm_4, eps, theta):
		self.pm_1 = SP.Symbol(pm_1)
		self.pm_2 = SP.Symbol(pm_2)
		self.pm_3 = SP.Symbol(pm_3)
		self.pm_4 = SP.Symbol(pm_4)
		self.theta = SP.Symbol(theta)
		self.eps = SP.Symbol(eps)
	
	def parameters(self):
		return self.pm_1, self.pm_2, self.pm_3, self.pm_4, self.theta, self.eps 
	
	def production_function(self, a, b):
		return self.pm_1 * a + self.pm_2 * b + self.eps

	def performance_measurement(self, a, b):
		return self.pm_3 * a + self.pm_4 * b + self.theta
	
	def payoff(self, outcome, wage):
		return outcome - wage

class Agent:
	def __init__(self, pm_1, pm_2):
		self.pm_1 = SP.Symbol(pm_1)
		self.pm_2 = SP.Symbol(pm_2)

	def parameters(self):
		return self.pm_1, self.pm_2

	def cost(self, a, b):
		return self.pm_1*(a**self.pm_2) + (1-self.pm_1)*(b**self.pm_2)

	def payoff(self, wage, a, b):
		return wage - self.cost(a, b)

	def contract(self, base_pay, commission, performance):
		return base_pay + commission * performance

if __name__ == "__main__":

	# choice variables for the agent (a_1 = a; a_2 = aa).
	a = SP.Symbol("a")
	aa = SP.Symbol("aa")
	
	# choice variables for the principal (s/base_pay = s; b/commission = b).
	s = SP.Symbol("s")
	b = SP.Symbol("b")

	# create objects.
	principal = Principal("f", "ff", "g", "gg", "eps", "theta")
	agent = Agent("bs", "es")

	# get the different equations - timing of the events.
	perf_measure = principal.performance_measurement(a, aa)
	wage = agent.contract(s, b, perf_measure)	

	# agent will maximize own payoff => optimal a and aa.
	agent_payoff = agent.payoff(wage, a, aa)
	target_function_a = SP.diff(agent_payoff, a)
	target_function_aa = SP.diff(agent_payoff, aa)
	optimal_a = solve(target_function_a, a)[0] # these should be unique solutions but are returned in lists => elegant way to solve this?
	optimal_aa = solve(target_function_aa, aa)[0]
	
	# which commission is efficient for payoff principal? => optimal b.
	production = principal.production_function(optimal_a, optimal_aa)
	cost = agent.cost(optimal_a, optimal_aa)
	welfare = production - cost
	target_function_b = SP.diff(welfare, b)
	target_function_b = target_function_b.subs("bs",0.5).subs("es",2)
	# only works if you plug in a value for the exponents (es)!!
	optimal_b = solve(target_function_b, b)

print(datetime.now() - startTime)