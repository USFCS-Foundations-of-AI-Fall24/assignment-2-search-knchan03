from mars_planner import *
from search_algorithms import *


if __name__=="__main__" :
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