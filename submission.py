from mars_planner import *
from routefinder import read_mars_graph
from search_algorithms import *


if __name__=="__main__" :

    print("Testing Mars Planner...\n")
    #move to sample
    print("Running BFS...")
    s1 = RoverState()  # Initial state at the station
    result1_bfs = breadth_first_search(s1, action_list, move_to_sample_goal)
    result1_dfs = depth_first_search(s1, action_list, move_to_sample_goal)
    result1_dls = depth_first_search(s1, action_list, move_to_sample_goal, 10)
    print("BFS: ", result1_bfs, "DFS: ", result1_dfs, "DLS with limit 10: ", result1_dls)

    #remove sample
    s2 = RoverState()
    result2_bfs = breadth_first_search(s2, action_list, remove_sample_goal)
    result2_dfs = depth_first_search(s2, action_list, remove_sample_goal)
    result2_dls = depth_first_search(s2, action_list, remove_sample_goal, 10)
    print("BFS: ", result2_bfs, "DFS: ", result2_dfs, "DLS with limit 10: ", result2_dls)
    
    #return to charger
    s3 = RoverState()
    result3_bfs = breadth_first_search(s3, action_list, return_to_charger_goal)
    result3_dfs = depth_first_search(s3, action_list, return_to_charger_goal)
    result3_dls = depth_first_search(s3, action_list, return_to_charger_goal, 10)
    print("BFS: ", result3_bfs, "DFS: ", result3_dfs, "DLS with limit 10: ", result3_dls)
    
    print("--------------------------------------------------------\nRoute Finder Tests\n")
    print("Testing Read Graph...\n")
    mars_graph = read_mars_graph("MarsMap.txt")
    mars_graph.print()