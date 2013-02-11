import strategies
import numpy as np

def scores(tuple, coop, defect, sucker, winner):
	strat_1 = tuple[0]
	strat_2 = tuple[1]
	if strat_1 == strat_2:
	    if strat_1 == 'C': return (coop, coop)
	    if strat_1 == 'D': return (defect, defect)
	if strat_1 == 'C': return (sucker, winner)
	return (winner, sucker)

class Agent():
    def __init__(self, strat):
        self.utility = []
        self.moves = [None]
        self.strategy = strat
    
    def move(self, iteration, opp_last_move):
        return self.strategy(iteration, opp_last_move)

# I need to add a way to choose the population you are playing against.
def get_payoffs(strategy, iterations, coop, defect, sucker, winner, complete_payoffs, weights):
    strategy_name_tuples = [(k, Agent(v)) for k,v in strategies.all.iteritems()]
    agent = Agent(strategy)
    list_of_strategies = []
    if weights:
        list_of_weights = []
    for strategy_name_tuple in strategy_name_tuples:
        strategy_name = strategy_name_tuple[0]
        opponent = strategy_name_tuple[1]
        list_of_strategies.append(strategy_name)
        if weights:
            list_of_weights.append(weights[strategy_name])
        i = 0
        while i < iterations:
            agent_move = agent.move(i, opponent.moves[-1])
            opponent_move = opponent.move(i, agent.moves[-1])
            result  = scores((agent_move, opponent_move), coop, defect, sucker, winner)
            agent.utility.append(result[0])
            opponent.utility.append(result[1])
            agent.moves.append(agent_move)
            opponent.moves.append(opponent_move)
            i+=1
    reshaped_utils = np.array(agent.utility).reshape(len(strategy_name_tuples), iterations)
    if weights:
        reshaped_utils = [np.dot(np.cumsum(reshaped_utils[i]), list_of_weights[i]) for i in range(len(reshaped_utils))]
    else:
        reshaped_utils = [np.cumsum(util) for util in reshaped_utils]
    ceiling = max([i[-1] for i in reshaped_utils])
    mean_payoff = np.mean(reshaped_utils, axis = 0).tolist()
    if not complete_payoffs:
        return mean_payoff
    else:
        data = {list_of_strategies[i]: reshaped_utils[i].tolist() for i in range(len(list_of_strategies))}
        return data, mean_payoff, ceiling

def get_all_strategies(iterations, coop, defect, sucker, winner, weights):
    output = {}
    for k,v in strategies.all.iteritems():
        payoff = get_payoffs(v, iterations, coop, defect, sucker, winner, False, weights)
        output[k] = payoff
    ceiling = max([i[-1] for i in output.values()])
    return output, ceiling