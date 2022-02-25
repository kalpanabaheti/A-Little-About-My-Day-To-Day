
SEARCHES

There are five baseline searches covered in this section, followed by a description of current research. 

1. Uniform Cost Search and Breadth-First Search - 

This is the first benchmark for exhaustive and accurate discovery of paths with no look-ahead. 

UCS Psuedocode -

    function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
     if problem's initial state is a goal then return empty path to initial state
     frontier ← a priority queue ordered by pathCost, with a node for the initial state
     reached ← a table of {state: the best path that reached state}; initially empty
     solution ← failure
     while frontier is not empty and top(frontier) is cheaper than solution do
       parent ← pop(frontier)
       for child in successors(parent) do
         s ← child.state
         if s is not in reached or child is a cheaper path than reached[s] then
           reached[s] ← child
           add child to the frontier
           if child is a goal and is cheaper than solution then
             solution = child
     return solution


2. A-Star search

This incorporates heuristics. Combining this with a strategy and heuristic framing from the game arena games would result in better cost functions. 

A* Psuedocode -

    function reconstruct_path(cameFrom, current)
        total_path := {current}
        while current in cameFrom.Keys:
            current := cameFrom[current]
            total_path.prepend(current)
        return total_path

    // A* finds a path from start to goal.
    // h is the heuristic function. h(n) estimates the cost to reach goal from node n.
    function A_Star(start, goal, h)
        // The set of discovered nodes that may need to be (re-)expanded.
        // Initially, only the start node is known.
        // This is usually implemented as a min-heap or priority queue rather than a hash-set.
        openSet := {start}

        // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
        // to n currently known.
        cameFrom := an empty map

        // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
        gScore := map with default value of Infinity
        gScore[start] := 0

        // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
        // how short a path from start to finish can be if it goes through n.
        fScore := map with default value of Infinity
        fScore[start] := h(start)

        while openSet is not empty
            // This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
            current := the node in openSet having the lowest fScore[] value
            if current = goal
                return reconstruct_path(cameFrom, current)

            openSet.Remove(current)
            for each neighbor of current
                // d(current,neighbor) is the weight of the edge from current to neighbor
                // tentative_gScore is the distance from start to the neighbor through current
                tentative_gScore := gScore[current] + d(current, neighbor)
                if tentative_gScore < gScore[neighbor]
                    // This path to neighbor is better than any previous one. Record it!
                    cameFrom[neighbor] := current
                    gScore[neighbor] := tentative_gScore
                    fScore[neighbor] := tentative_gScore + h(neighbor)
                    if neighbor not in openSet
                        openSet.add(neighbor)

        // Open set is empty but goal was never reached
        return failure
    
3. UCS Bidirectional and A-Star Bidirectional 
    
These searches involve simultaneous search from the start and goal node and have a bounded condition upon which the path search may be terminated. Please find the bounded relation clauses here - https://en.wikipedia.org/wiki/A*_search_algorithm

For bidirectional searches - the criteria to terminate is when the sum of paths from both ends start increasing instead of decsreasing with each iteration.

4. Tridirectional A-Star

The tridirectional A* implemented uses a third pre-set node to be traversed mandatorily on the path. This node might be an efficiency checkpoint discovered from past iterations and so on. 

Research - 

Improving tridirectional search involves the following - 
~ applying the triangular inequality wherever possible
~ deducing the best landmarks as the the third node to be used
~ framing more accurate heuristic cost functions

