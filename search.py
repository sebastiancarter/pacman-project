# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

    """
    This is the SearchNode class for easily tracking the path to and location of a state
    """

class SearchNode:
    '''
    The SearchNode contains a tuple for storing location
    and a list for storing the list of actions to a location from the start
    '''
    def __init__(self):
        self.location = tuple()
        self.actions_to_here = []

    #act() and loc() were used for debugging purposes.
    def act(self):
        for action in self.actions_to_here:
            print(action)

    def loc(self):
        print(self.location)

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    startState = problem.getStartState()
    visited = set()
    fringe = util.Stack()
    
    startNode = (startState, "", 0)
    # we add the starting node and a list, 
    # which holds the actions it took to get to the node to the fringe
    fringe.push((startNode, []))
    while not fringe.isEmpty(): # while the fringe is not empty
        (currNode, currPlan) = fringe.pop()
        (currState, currAction, currCost) = currNode

        if problem.isGoalState(currState):
            return currPlan

        if currState not in visited:
            visited.add(currState)
            successors = problem.getSuccessors(currState)
            for node in successors:
                (newState, newAction, newCost) = node
                newPlan = currPlan.copy() 
                newPlan.append(newAction) # add action to the plan
                fringe.push((node, newPlan))
        
        
    print("goal not found")
    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    startState = problem.getStartState()
    visited = set()
    fringe = util.Queue()

    startNode = (startState, "", 0)
    # we add the starting node and a list, 
    # which holds the actions it took to get to the node to the fringe
    fringe.push((startNode, []))
    while not fringe.isEmpty(): # while the fringe is not empty
        (currNode, currPlan) = fringe.pop()
        (currState, currAction, currCost) = currNode

        if problem.isGoalState(currState):
            return currPlan

        if currState not in visited:
            visited.add(currState)
            successors = problem.getSuccessors(currState)
            for node in successors:
                (newState, newAction, newCost) = node
                newPlan = currPlan.copy()
                newPlan.append(newAction) # add action to the plan
                fringe.push((node, newPlan))
        
    print("goal not found")
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    visited = set()
    fringe = util.PriorityQueue()
    
    bigCost = 0
    startNode = (startState, "", bigCost)
    # we add the starting node and a list, 
    # which holds the actions it took to get to the node to the fringe
    fringe.push((startNode, [], 0), bigCost) # we use the cumulative
    #                                        # cost for the priorityQueue
    while not fringe.isEmpty(): # while the fringe is not empty
        (currNode, currPlan, totCost) = fringe.pop()
        (currState, currAction, currCost) = currNode

        if problem.isGoalState(currState):
            return currPlan

        if currState not in visited:
            visited.add(currState)
            successors = problem.getSuccessors(currState)
            for node in successors:
                (newState, newAction, newCost) = node
                newPlan = currPlan.copy()
                newTotalCost = totCost + newCost
                newPlan.append(newAction) # add action to the plan
                fringe.push((node, newPlan, newTotalCost), newTotalCost)
        
        
    print("goal not found")
    return None



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    startState = problem.getStartState()
    visited = set()
    fringe = util.PriorityQueue()
    print(heuristic)
    
    bigCost = 0
    aStarCost = bigCost + heuristic(startState, problem) # f(n) = g(n) + h(n)
    startNode = (startState, "", bigCost)
    # we use the astar cost for the priority queue
    fringe.push((startNode, [], 0), aStarCost)
    while not fringe.isEmpty(): # while the fringe is not empty
        (currNode, currPlan, totCost) = fringe.pop()
        (currState, currAction, currCost) = currNode

        if problem.isGoalState(currState):
            return currPlan

        if currState not in visited:
            visited.add(currState)
            successors = problem.getSuccessors(currState)
            for node in successors:
                (newState, newAction, newCost) = node
                newPlan = currPlan.copy()
                newTotalCost = totCost + newCost
                aStarCost = newTotalCost + heuristic(newState, problem)
                newPlan.append(newAction) # add action to the plan
                fringe.push((node, newPlan, newTotalCost), aStarCost)
        
        
    print("goal not found")
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
