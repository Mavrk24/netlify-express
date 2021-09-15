import sys
import os

class MDP(object):
    def __init__(self, N):
        self.N = N
    def startState(self, state):
        return state == self.N
    def isEnd(self, state):
        return 0
    def Actions(self, state):
        actions = []
        if state-12 > 0 :
            actions.append('stretch')
            actions.append('ergonomic')
        else:
            actions.append('none')
        return actions
    def SProbReward (self,state,action):
        result = []
        cost = [60,30]
        target ='shoulder'
        reward = [10.84,9.135,11.76, 8.93]
        if (action == 'ergonomic') and (target == 'neck'):
            result.append((state, 1. , 0))
        elif (action == 'ergonomic') and (target == 'shoulder'):
            result.append((state-9, 0.17 , reward[1] ))
            result.append((state, 0.83 , -cost[0]))
        elif (action == 'stretch') and (target == 'neck'):
            result.append((state-12, 0.05 , reward[2] ))
            result.append((state, 0.95 , 0 ))
        elif (action == 'stretch') and (target == 'shoulder'):
            result.append((state-9, 0.05 , reward[3] ))
            result.append((state, 0.95 , -cost[1]))
        return result
    def discount(self):
        return 1
    def states(self):
        return range (1, self.N+1)

def valueiteration(MDP):
    V = {}
    for state in MDP.states():
        V[state] = 0.

    def Q(state, action):
        return sum(prob*(reward + MDP.discount()*V[newState]) for newState, prob, reward in MDP.SProbReward(state,action))
    while True:
        newV = {}
        for state in MDP.states():
            if MDP.isEnd(state):
                newV[state]=0.
            else: 
                newV[state]= max(Q(state,action) for action in MDP.Actions(state))
        if max(abs(V[state]-newV[state]) for state in MDP.states())<1e-10:
            break
        V = newV
        pi = {}
        for state in MDP.states():
            if MDP.isEnd(state):
                pi[state]='none'
            else:
                pi[state] = max((Q(state,action),action) for action in MDP.Actions(state))[1]
        print('{:15}{:15}{:15}'.format('s','V','pi(s)'))
        for state in MDP.states():   
            print('{:15}{:15}{:15}'.format(state,V[state],pi[state]))
    return pi
