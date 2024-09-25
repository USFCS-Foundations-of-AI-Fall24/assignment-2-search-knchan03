import math
from queue import PriorityQueue

from Graph import Graph, Node, Edge

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'
    
    def neighbors(self, heuristic_fn):
        neighbors = []
        for edge in self.mars_graph.get_edges(Node(self.location)):
            location = edge.dest.value
            neighbor = map_state(location, self.mars_graph, prev_state = self)
            neighbor.g = self.g + edge.val
            neighbor.h = heuristic_fn(neighbor)
            neighbor.f = neighbor.g + neighbor.h
            neighbors.append(neighbor)
        return neighbors


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    num_states_generated = 0

    while not search_queue.empty():
        current_state = search_queue.get()
        if goal_test(current_state):
            print("Goal Found!\nNumber of States generated: ", num_states_generated)
            return current_state
        else :
            neighbors = current_state.neighbors(heuristic_fn)
            if use_closed_list: 
                filtered_neighbors = []
                for neighbor in neighbors: 
                    if neighbor not in closed_list:
                        filtered_neighbors.append(neighbor)
                neighbors = filtered_neighbors
                for neighbor in neighbors : 
                    num_states_generated += 1
                    closed_list[neighbor] = True
                    search_queue.put(neighbor)
    print("Goal Not Found\n", num_states_generated)
    return None # goal not found


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    x1, y1 = map(float, state.location.split(','))
    x2, y2 = 1.0, 1.0
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    mars_graph = Graph()
    nodes = {} #dict to keep nodes unique
    with open(filename, 'r') as file:
        for line in file:
            key, nodes_val = line.strip().split(":")
            node = key.strip()
            neighbors = nodes_val.strip().split()

            if node not in nodes: #check if already in dict
                nodes[node] = Node(node)
                mars_graph.add_node(nodes[node])

            for neighbor in neighbors:
                if neighbor not in nodes:
                    nodes[neighbor] = Node(neighbor)
                    mars_graph.add_node(nodes[neighbor])
                mars_graph.add_edge(Edge(nodes[node], nodes[neighbor]))
    return mars_graph