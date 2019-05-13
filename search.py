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

    # stack to hold the fringe
    fringe_ds = util.Stack()

    # Initializing the current state and feeding the start state value to it 
    present_state = problem.getStartState()
    
      
    # Add a list along with the state to store the list of actions to get to the present_state
    fringe_ds.push((present_state, []))
    position_visited = []
      

    # Loop to check if there are any elements left in the stack. We are implementing the DFS iteratively instead of recursively
    while not fringe_ds.isEmpty():
        present_state, state_action = fringe_ds.pop()       # If fringe_ds is not empty, popping elements from the stack
        position_visited.append(present_state)                 # Counting the visited nodes

        # Checking if current node is the goal node
        if problem.isGoalState(present_state):
            return state_action

        successors_list = problem.getSuccessors(present_state) # List of successors

        if [] != successors_list:
            for item in successors_list:
                new_state, dirn, cost = item
                if new_state not in position_visited:                     # Checking whether the element/vertex has been discovered already
                    fringe_ds.push((new_state, state_action + [dirn]))              # If the vertex has not been visited already, then it is pushed onto the fringe_ds
    return []                                                                       # Returning an empty list


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # Queue to hold the fringe
    fringe_ds = util.Queue()

    # Initializing the current state and feeding the start state value to it 
    present_state = problem.getStartState()
    
    # Add a list along with the state to store the list of actions to get to the present_state
    fringe_ds.push((present_state, []))
    position_visited = [present_state]
    

    # Loop to check if there are any elements left in the stack. We are implementing the BFS iteratively instead of recursively
    while not fringe_ds.isEmpty():
        present_state, state_action = fringe_ds.pop()               # If fringe_ds is not empty, dequeue elements from it

        # Checking if current node is the goal node
        if problem.isGoalState(present_state):
            return state_action

        successors_list = problem.getSuccessors(present_state)        # List of successors


        if [] != successors_list:
            for item in successors_list:
                new_state, dirn, cost = item
                if new_state not in position_visited:                           # Checking whether the element/vertex has been discovered already
                    position_visited.append(new_state)                     
                    fringe_ds.push((new_state, state_action + [dirn]))     # If the vertex has not been visited already, then it is pushed onto the fringe_ds     
    return []                                                                   # Returning an empty list

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Creating a priority Queue to hold the open set
    priority_queue = util.PriorityQueue()
    present_state = problem.getStartState()

    # Add the present_state to the open priority_queue
    priority_queue.push((present_state, [], list()), 0)

    while not priority_queue.isEmpty():                                          # If priority queue is not empty, dequeue elements from it
        node, state_action, visited = priority_queue.pop()
        if node in visited: continue                                             # Continue if the node has already been visited
        if problem.isGoalState(node): return state_action                        # Checking if the current node is the goal node, if it is, return the goal node
        visited.append(node)
        for co, dirn, _ in problem.getSuccessors(node):
            n_actions = state_action + [dirn]
            priority_queue.push((co, n_actions, visited), problem.getCostOfActions(n_actions))      # Inserting all the children of the dequeued element, with the cumulative costs as priority
    return []                                                                                       # Returning an empty list

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # Creating a priority Queue to hold the open set
    priority_queue = util.PriorityQueue()
    present_state = problem.getStartState()


    # Add the present_state to the open priority_queue
    priority_queue.push((present_state, [], list()), 0)


    while not priority_queue.isEmpty():                                     # If priority queue is not empty, dequeue elements from it
        node, state_action, visited = priority_queue.pop()


        if node in visited: continue                                         # Continue if the node has already been visited
        if problem.isGoalState(node): return state_action                    # Checking if the current node is the goal node, if it is, return the goal node
        visited.append(node)
        for co, dirn, _ in problem.getSuccessors(node):
            n_actions = state_action + [dirn]
            cost = problem.getCostOfActions(n_actions) + heuristic(co, problem)

            priority_queue.push((co, n_actions, visited), cost)
            
    return []                                                               # Returning an empty list


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch








