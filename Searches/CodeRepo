# coding=utf-8

import heapq
import os
import pickle
import math
import copy


class PriorityQueue(object):
    """
    Attributes:
        queue (list): Nodes added to the priority queue - manipulated by heap popping, hence path states can be stored along with the node.
    """

    def __init__(self):
        """Initialize a new Priority Queue."""

        self.queue = []

    def pop(self):
        """
        Pops the top priority node from queue.

        Returns:
            The node with the highest priority.
        """
        fifo = dict()
        temp = list()

        for node in self.queue:

            key = node[0]

            if str(key) not in fifo.keys():

                temp.append(node)
                fifo[str(key)]=[]

            else:

                fifo[str(key)].append(node)

        
        heapq.heapify(temp)
        

        newl = list()

        for first in temp:

            l = [first]
            for other in fifo[str(first[0])]:

                l.append(other)

            newl.extend(l)


        top = newl.pop(0)
        self.queue = newl

        return top

    def remove(self, node):
        """
        Removes a node from the queue.

        Args:
            node (tuple): The node to remove from the queue.
        """
        self.queue.remove(node)
        return
        

    def __iter__(self):
        """Queue iterator."""

        return iter(sorted(self.queue))

    def __str__(self):
        """Convert PQ to string."""

        return 'PQ:%s' % self.queue

    def append(self, node):
        """
        Appends a node to the queue.

        Args:
            node: Comparable Object to be added to the priority queue.
        """
        self.queue.append(node)
        return
        
        
    def __contains__(self, key):
        """
        Check operator for 'in'

        Args:
            key: The key to check for in the queue.

        Returns:
            True if key is found in queue, False otherwise.
        """

        return key in [n[0] for n in self.queue]

    def __eq__(self, other):
        """
        Compares this PQ with another PQ.

        Args:
            other (PriorityQueue): Priority Queue to compare against.

        Returns:
            True if the two priority queues are equivalent.
        """

        return self.queue == other.queue

    def size(self):
        """
        Gets the current size of the queue.

        Returns:
            Integer of number of items in queue.
        """

        return len(self.queue)

    def clear(self):
        """Reset queue to empty"""

        self.queue = []

    def top(self):
        """
        Gets top item in the queue.

        Returns:
            The first item stored in the queue.
        """

        return self.queue[0]


def get_graph(file):

    #Takes pickled raph file as argument and returns navigable graph. 

    infile = open(file,'rb')
    d = pickle.load(infile)
    infile.close()

    return d


def breadth_first_search(graph, start, goal):
    """

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """
    
    if start==goal:
        return []
    
        
    q = [[start]]
    visited=[]

    while len(q)>0:
           
        s = q.pop(0)
        last = s[-1]
        

        if last not in visited:
            neighbours = sorted(graph[last])
             
            for neighbour in neighbours:
                update = list(s)
                update.append(neighbour)
                q.append(update)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    #print("Shortest path = ", *new_path)
                    return update
                
            visited.append(last)



def uniform_cost_search(graph, start, goal):
    """
    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """
    if start == goal:
        return []
    
    
    first_node = [0,start,[start]]
    pq = PriorityQueue()
    pq.append(first_node)
    explored = set()
    count = 0
    
    while pq.size()!=0:
        
        current = pq.pop()
        curr_cost = current[0]
        curr_node = current[1]
        curr_sol = current[2]
        
        if curr_node == goal:
            return curr_sol
        
        
        if curr_node not in explored:
            
            nbs = graph[curr_node]
            count+=1

            for nb in nbs:


                new_cost = curr_cost + graph.get_edge_weight(curr_node, nb)
                new_sol = curr_sol + [nb]
                new_node = [new_cost,nb,new_sol]

                if nb not in explored and new_node not in pq:

                    pq.append(new_node)

                for node in pq:

                    if node[1] == nb and node[0] > new_cost:

                        pq.remove(node)
                        pq.append(new_node)
                        break

            explored.add(curr_node)
        
    return False
   

def null_heuristic(graph, v, goal):
    """
    Null heuristic used as a base line.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        v (str): Key for the node to calculate from.
        goal (str): Key for the end node to calculate to.

    Returns:
        0
    """

    return 0


def euclidean_dist_heuristic(graph, v, goal):
    """
    Args:
        graph (ExplorableGraph): Undirected graph to search.
        v (str): Key for the node to calculate from.
        goal (str): Key for the end node to calculate to.

    Returns:
        Euclidean distance between `v` node and `goal` node
    """
    current = graph.nodes[v]['pos']
    goal = graph.nodes[goal]['pos']
    
    dist_square = ((goal[1]-current[1])**2) + ((goal[0]-current[0])**2)
    dist = abs(dist_square ** 0.5)
    return dist


def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    """

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.
        heuristic: Function to determine distance heuristic.
            Default: euclidean_dist_heuristic.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """
    
    if start == goal:
        return []
    
    h = heuristic(graph,start,goal)
    first_node = [h,start,[start],0]
    pq = PriorityQueue()
    pq.append(first_node)
    explored = set()
    
    
    while pq.size()!=0:
        
        current = pq.pop()
        curr_hcost = current[0]
        curr_node = current[1]
        curr_sol = current[2]
        curr_cost = current[3]
        
        if curr_node == goal:
            
            return curr_sol
        
        
        if curr_node not in explored:
            
            nbs = graph[curr_node]

            for nb in nbs:


                cost1 = graph.get_edge_weight(curr_node, nb)
                cost2 = heuristic(graph,nb,goal)
                without_h = curr_cost + cost1
                new_cost = without_h + cost2
                
                new_sol = curr_sol + [nb]
                new_node = [new_cost,nb,new_sol,without_h]

                if nb not in explored and new_node not in pq:

                    pq.append(new_node)

                for node in pq:

                    if node[1] == nb and node[0] > new_cost:

                        pq.remove(node)
                        pq.append(new_node)
                        break

            explored.add(curr_node)
        
    return False


def bidirectional_ucs(graph, start, goal):
    """

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """
    
    def proceed(dn,frontier,primary,rcheck,graph):


        curr = frontier.pop()
    
        cost = curr[0]
        node = curr[1]
        path = curr[2]
        
        solution = False
        low = 10**8

        if node not in primary.keys():

            primary[node] = (cost,path)
            nbs = graph[node]

            for nb in nbs:
                
                if nb not in path:

                    new_cost = cost + graph.get_edge_weight(node, nb)
                    new_path = path + [nb]
                    new_node = (new_cost,nb,new_path)
                    frontier.append(new_node)


                    if nb in primary.keys() and primary[nb][0]>new_cost:
                        primary[nb] = (new_cost,new_path)


            for n1 in rcheck.keys():
                
                for n2 in primary.keys():

                    if n1==n2:

                        new_path = primary[n2][1]

                        other = rcheck[n1][1]
                        total_cost = primary[n2][0] + rcheck[n1][0]

                        if dn == 'F':
                            soln = new_path[:-1]
                            soln.extend(other[::-1])

                        else:
                            soln = new_path[::-1]
                            soln = other + soln[1:]

                        if total_cost<low:
                            solution = (total_cost,soln)
                            low = total_cost

        return solution
        
    #main function
    
    if start == goal:
        return []
    
    if graph.get_edge_data(start,goal)!=None:
        return [start,goal]
    
    nodef = [0,start,[start]]
    nodeb = [0,goal,[goal]]
    
    qf = PriorityQueue()
    qb = PriorityQueue()
    
    qf.append(nodef)
    qb.append(nodeb)
    
    reachedf = dict()
    reachedb = dict()
    solution = False
    
    mu = 10**8
    
    topf = qf.top()
    topb = qb.top()
    flag = 0
    
    while topf[0]+topb[0]<=2*mu and qf.size()!=0 and qb.size()!=0: #topf[0]+topb[0]<mu
        
        if topf[0]<=topb[0]:
            
            #print('f: ',qf)
            temp = proceed('F',qf,reachedf,reachedb,graph)
            #print('f: ',temp)
            if temp!=False and temp[1][-1] == goal and temp[0]<mu:
                mu = temp[0]
                solution = temp[1]
                flag+=1
            
        else:
            
            #print('b: ',qb)
            temp = proceed('B',qb,reachedb,reachedf,graph)
            #print('b: ',temp)
            if temp!=False and temp[1][0] == start and temp[0]<mu:
                mu = temp[0]
                solution = temp[1]
                flag+=1
                
        if qf.size()!=0 and qb.size()!=0:      
            topf = qf.top()
            topb = qb.top()
                
    return solution



def bidirectional_a_star(graph, start, goal,
                         heuristic=euclidean_dist_heuristic):
    """

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.
        heuristic: Function to determine distance heuristic.
            Default: euclidean_dist_heuristic.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """
    
        
    def proceedastar(dn,frontier,primary,rcheck,graph,heuristic,start,goal):

        curr = frontier.pop()
    
        hcost = curr[0]
        node = curr[1]
        path = curr[2]
        actcost = curr[3]
        
        solution = False
        low = 10**8

        if node not in primary.keys():

            primary[node] = (hcost,path,actcost)
            nbs = graph[node]

            for nb in nbs:
                
                if nb not in path:

                    if dn == 'F':
                        h = heuristic(graph,nb,goal)
                    else:
                        h = heuristic(graph,nb,start)

                    without_h = actcost + graph.get_edge_data(node, nb)['weight']
                    
                    new_cost = without_h + h
                    new_path = path + [nb]
                    new_node = [new_cost,nb,new_path,without_h]
                    frontier.append(new_node)

                    if nb in primary.keys() and primary[nb][0]>new_cost:
                        primary[nb] = (new_cost,new_path,without_h)
                        

            for n1 in rcheck.keys():
                
                for n2 in primary.keys():
                    
                    if n1==n2:
                        
                        new_path = primary[n2][1]

                        other = rcheck[n1][1]
                        total_cost = primary[n2][2] + rcheck[n1][2]

                        if dn == 'F':
                            soln = new_path[:-1]
                            soln.extend(other[::-1])

                        else:
                            soln = new_path[::-1]
                            soln = other + soln[1:]
                        
                        if total_cost<low:
                            solution = (total_cost,soln)
                            low = total_cost
                    
        return solution

    #main function
    
    if start == goal:
        return []
    
    if graph.get_edge_data(start,goal)!=None:
        return [start,goal]
    
    h1 = heuristic(graph,start,goal)
    h2 = heuristic(graph,goal,start)
    nodef = [h1,start,[start],0]
    nodeb = [h2,goal,[goal],0]
    
    qf = PriorityQueue()
    qb = PriorityQueue()
    
    qf.append(nodef)
    qb.append(nodeb)
    
    reachedf = dict()
    reachedb = dict()
    solution = False
    
    mu = 10**8
    
    topf = qf.top()
    topb = qb.top()
    flag = 0
    
    while topf[3]+topb[3]<=2*mu and qf.size()!=0 and qb.size()!=0:  
        
        if topf[0]<=topb[0]:
            #print('f: ',qf)
            temp = proceedastar('F',qf,reachedf,reachedb,graph,heuristic,start,goal)
            #print('f: ',temp)
            if temp!=False and temp[1][-1] == goal and temp[0]<mu:
                mu = temp[0]
                solution = temp[1]
                flag+=1
            
        else:
            
            #print('b: ',qb)
            temp = proceedastar('B',qb,reachedb,reachedf,graph,heuristic,start,goal)
            #print('b: ',temp)
            if temp!=False and temp[1][0] == start and temp[0]<mu:
                mu = temp[0]
                solution = temp[1]
                flag+=1
                
        if qf.size()!=0 and qb.size()!=0:
            topf = qf.top()
            topb = qb.top()
                
    return solution
    


def tridirectional_search(graph, goals): #RESEARCH BASELINE
    """
    Args:
        graph (ExplorableGraph): Undirected graph to search.
        goals (list): Key values for the 3 goals

    Returns:
        The best path as a list from one of the goal nodes (including both of
        the other goal nodes).
    """
    
    init_check = set(goals)
    if len(init_check) == 1:
        #print('case 1')
        return []
    
    elif len(init_check) == 2:
        l = list(init_check)
        s = l[0]
        g = l[1]
        answer = uniform_cost_search(graph,s,g)
        #print('case 2:',answer)
        return answer
    
    start1 = goals[0]
    start2 = goals[1]
    start3 = goals[2]
    
    pq = PriorityQueue()
    
    node1 = [0,start1,[start1],'1']
    node2 = [0,start2,[start2],'2']
    node3 = [0,start3,[start3],'3']
    
    pq.append(node1)
    pq.append(node2)
    pq.append(node3)
    
    explored1 = set()
    explored2 = set()
    explored3 = set()
    
    explored = {'1':explored1,'2':explored2,'3':explored3}
    
    paths = []
    true_check = []
    
    while pq.size()!=0:
        
        current = pq.pop()
        curr_cost = current[0]
        curr_node = current[1]
        curr_sol = current[2]
        curr_team = current[3]
        
        if (curr_node == start1 or curr_node == start2 or curr_node == start3) and curr_node!=curr_sol[0] and set([curr_sol[0],curr_sol[-1]]) not in true_check:
            
            paths.append(curr_sol)
            true_check.append(set([curr_sol[0],curr_sol[-1]]))
            
            if len(paths) == 2:
                
                path1 = paths[0]
                path2 = paths[1]
                
                if path1[0] == path2[-1]:
                    path = path2 + path1[1:]
                    
                elif path2[0] == path1[-1]:
                    path = path1 + path2[1:]
                    
                elif path1[0] == path2[0]:
                    path = path1[::-1] + path2[1:]
                    
                elif path1[-1] == path2[-1]:
                    path = path1[:-1] + path2[::-1]
                    
                #print('case 3:',path)
                return path
        
        
        if curr_node not in explored[curr_team]:
            
            nbs = graph[curr_node]

            for nb in nbs:


                new_cost = curr_cost + graph.get_edge_weight(curr_node, nb)
                new_sol = curr_sol + [nb]
                new_node = [new_cost,nb,new_sol,curr_team]

                if nb not in explored[curr_team] and new_node not in pq:

                    pq.append(new_node)

                for node in pq:

                    if node[1] == nb and node[3] == curr_team and node[0] > new_cost:

                        pq.remove(node)
                        pq.append(new_node)
                        break

            explored[curr_team].add(curr_node)
        
    
    return False
   

def haversine_dist_heuristic(graph, v, goal):
    """
    Alternate heuristic -
    
    Args:
        graph (ExplorableGraph): Undirected graph to search.
        v (str): Key for the node to calculate from.
        goal (str): Key for the end node to calculate to.

    Returns:
        Haversine distance between `v` node and `goal` node
    """

    #Load latitude and longitude coordinates in radians:
    vLatLong = (math.radians(graph.nodes[v]["pos"][0]), math.radians(graph.nodes[v]["pos"][1]))
    goalLatLong = (math.radians(graph.nodes[goal]["pos"][0]), math.radians(graph.nodes[goal]["pos"][1]))

    constOutFront = 2*6371 #Radius of Earth = 6,371 kilometers
    term1InSqrt = (math.sin((goalLatLong[0]-vLatLong[0])/2))**2 
    term2InSqrt = math.cos(vLatLong[0])*math.cos(goalLatLong[0])*((math.sin((goalLatLong[1]-vLatLong[1])/2))**2) 
    
    return constOutFront*math.asin(math.sqrt(term1InSqrt+term2InSqrt)) 
    
    
