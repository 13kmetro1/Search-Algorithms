# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class superlist(object):
    def __init__(self,lol,xd):
        self.lol = lol
        self.xd = xd
class supernode(object):
    def __init__(self,lol,xd,cost):
        self.lol = lol
        self.xd = xd
        self.cost = cost
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
    "*** YOUR CODE HERE ***"
    
    import copy
    stack = []
    first = superlist([],[problem.getStartState()])
    stack.append(first)
    if problem.isGoalState(problem.getStartState()):
        
        return first.lol
    
    while not len(stack) == 0:
        
        current = stack.pop()
        currentd = current.xd[-1]
        #if(current == problem.getStartState()):
            #print 'hi'
        try:
            if problem.isGoalState(current.xd[-1]):            
                return current.lol
        except TypeError or AttributeError:
                return current.lol
        else:
            adj = problem.getSuccessors(currentd)
            for x in adj:
                    if not x[0] in current.xd:
                        newdir = copy.copy(current.lol)
                        newdir.append(x[1])
                        newloc = copy.copy(current.xd)
                        newloc.append(x[0])
                        jpg = superlist(newdir,newloc)
                        stack.append(jpg)
                      
    return []
            


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    first = superlist([],[problem.getStartState()])
    import copy
    q = util.Queue()
    
    if problem.isGoalState(problem.getStartState()):        
        return first.lol
    q.push(first)
    visited = [problem.getStartState()]
    
    while not q.isEmpty():
        current = q.pop()
        let = current.xd[-1]
        try:
            if problem.isGoalState(let):           
                return current.lol
        except TypeError:
            return current.lol
        adj = problem.getSuccessors(let)
        for x in adj:
            if (not x[0] in current.xd) and (not x[0] in visited):
                try:
                    if not problem.isGoalState(x[0]):
                        visited.append(x[0])
                except TypeError:
                    pass
                jpg = superlist(copy.copy(current.lol),copy.copy(current.xd))
                jpg.lol.append(x[1])
                jpg.xd.append(x[0])                
                q.push(jpg)
    return[]
                
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
   
    import copy
    first = supernode([],[problem.getStartState()],0)
    pq = util.PriorityQueue()
    if problem.isGoalState(problem.getStartState()):        
        return first.lol
    visited = [problem.getStartState()]
    pq.push(first,0)
    while not pq.isEmpty():
        current = pq.pop()
        topnode = len(current.xd)-1
        let = current.xd[topnode]
        try:
            if problem.isGoalState(let):           
                return current.lol
        except TypeError:
            return current.lol
        for x in problem.getSuccessors(let):
            if not x[0] in visited and not x[0] in current.xd:
                newcost = (x[2]) + current.cost
                jpg = supernode(copy.copy(current.lol),copy.copy(current.xd),newcost)
                jpg.lol.append(x[1])
                jpg.xd.append(x[0])                
                pq.push(jpg,jpg.cost)
                
                if problem.isGoalState(x[0]):
                    print "goal state"
                else:
                    visited.append(x[0])
     
    return []
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    import copy
    first = supernode([],[problem.getStartState()],0)
    pq = util.PriorityQueue()
    if problem.isGoalState(problem.getStartState()):        
        return first.lol
    visited = [problem.getStartState()]
    pq.push(first,0)
    while not pq.isEmpty():
        current = pq.pop()
        let = current.xd[-1]
        try:
            if problem.isGoalState(let):           
                return current.lol
        except TypeError:
            return current.lol
        for x in problem.getSuccessors(let):
            if not x[0] in visited and not x[0] in current.xd:
                if not problem.isGoalState(x[0]):
                        visited.append(x[0])
                newcost = (x[2]) + current.cost
                jpg = supernode(copy.copy(current.lol),copy.copy(current.xd),newcost)
                jpg.lol.append(x[1])
                jpg.xd.append(x[0])               
                newh = heuristic(x[0],problem)
                newcost = newcost + newh
                
                pq.push(jpg,newcost)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
