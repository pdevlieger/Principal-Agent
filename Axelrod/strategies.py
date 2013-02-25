##  I could not find the actual original strategies, so I made up some other (simple)   ##
##  strategies. These strategies do not represent the actual Axelrod tournament!        ##

from random import randint, choice

def tit_for_tat(iteration, opp_last_move):
    """Cooperate first, then play opponent's last move"""
    return 'C' if iteration == 0 else opp_last_move

def always_C(iteration, opp_last_move):
    """Always cooperate"""
    return 'C'

def always_D(iteration, opp_last_move):
    """Always defect"""
    return 'D'

def randomizer(iteration, opp_last_move):
    """Play a random strategy"""
    return choice(['D', 'C'])

def switch_C(iteration, opp_last_move):
    """Start with C, switch strategies after that."""
    return 'C' if iteration % 2 == 0 else 'D'

def switch_D(iteration, opp_last_move):
    """Start with D, switch strategies after that."""
    return 'D' if iteration % 2 == 0 else 'C'

def nasty_tft(iteration, opp_last_move):
    """Defect first, then play opponent's last move"""
    return 'D' if iteration == 0 else opp_last_move

def stubborn(iteration, opp_last_move):
    """Cooperate, until opponent defects. Then always defect"""
    if iteration == 0 or opp_last_move == 'C':
        return 'C'
    else:
        return 'D'

def play_70C(iteration, opp_last_move):
    """Cooperate 70% of the time."""
    return 'C' if randint(0, 9) < 7 else 'D'

def play_70D(iteration, opp_last_move):
    """Defect 70% of the time."""
    return 'D' if randint(0, 9) < 7 else 'C'

all = {'tft': tit_for_tat, 'ac': always_C, 'ad': always_D, 'rand': randomizer,
       'c_switch': switch_C, 'd_switch': switch_D, 'ntft': nasty_tft,
       'c_until_d': stubborn, 'c_70': play_70C, 'd_70': play_70D}
