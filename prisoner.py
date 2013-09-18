#! /usr/bin/python
#from random import randint
from random import getrandbits

def human_input():
    bid = None
    while bid != True or False:
        bid = raw_input("True or False? : >")
        print bid
        if 't' in bid:
            bid = True
        elif 'f' in bid:
            bid = False
        else:
            "Try: t/f, T/F, true/false, True/False"
        print "bid!", bid
        return bid

def random_strategy():
    return not getrandbits(1)

def payoff_matrix(strategy):
    if strategy == [True, True]:
        payoff = 3, 3
    elif strategy == [True, False]:
        payoff = 0, 5
    elif strategy == [False, True]:
        payoff = 5, 0
    elif strategy == [False, False]:
        payoff = 1, 1
    else:
        print "What the hell happened?"
    return payoff

def favor_finder(strategy, favor):
    favor[0] += int(strategy[0])
    favor[1] += int(strategy[1])
    return favor

def iterator():
    favor = [0, 0]
    interaction = 0
    interaction_limit = 8
    score = [0, 0]
    prev_strategy = [random_strategy(), random_strategy()]
    while interaction != interaction_limit:
        #strategy = [prev_strategy[1], human_input()]
        strategy = [random_strategy(), human_input()]
        score = [x + y for x, y in zip(score, payoff_matrix(strategy))]
        favor = favor_finder(strategy, favor)
        print "interaction: ", interaction
        print "   strategy: ", strategy
        print "      favor: ", favor
        print "      score: ", score
        print "\n"
        interaction += 1
        prev_strategy = strategy
    return score


def main():
    '''Prisoner's Dilemma
    '''
    iterator()

if __name__ == '__main__':
    main() 


