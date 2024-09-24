from mars_planner import *
from routefinder import read_mars_graph
from search_algorithms import *


if __name__=="__main__" :
    print("Mars Planner Tests\n")
    #BFS
    print("Running BFS...")
    s1 = RoverState()
    result1 = breadth_first_search(s1, action_list, mission_complete)
    print(result1, "\n")

    #DFS
    print("Running DFS...")
    s2 = RoverState()
    result2 = depth_first_search(s2, action_list, mission_complete)
    print(result2, "\n")
    
    #DLS
    print("Running DLS with depth limit of 10...")
    s3 = RoverState()
    result3 = depth_first_search(s3, action_list, mission_complete, 10)
    print(result3, "\n")

    print("--------------------------------------------------------\nRoute Finder Tests\n")
    print("Testing Read Graph...\n")
    mars_graph = read_mars_graph("MarsMap.txt")
    mars_graph.print()