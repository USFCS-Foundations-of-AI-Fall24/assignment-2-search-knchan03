from mars_planner import *
from routefinder import a_star, h1, map_state, read_mars_graph, sld
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

    print("\nTesting A* with \"8,8\" as start location...\n")
    start_state = map_state(location="8,8", mars_graph=mars_graph)
    astar_result = a_star(start_state, sld, map_state.is_goal)
    if astar_result:
        path = []
        state = astar_result
        while state is not None:
            path.append(state)
            state = state.prev_state
        path.reverse()
        for state in path:
            print(state.location)
    else:
        print("No path found")

    print("\nTesting UCS with \"8,8\" as start location...\n")
    ucs_result = a_star(start_state, h1, map_state.is_goal)
    if ucs_result:
        path = []
        state = ucs_result
        while state is not None:
            path.append(state)
            state = state.prev_state
        path.reverse()
        for state in path:
            print(state.location)
    else:
        print("No path found")