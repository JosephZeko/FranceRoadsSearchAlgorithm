#!/usr/bin/python3
from Data import *
from Node import *

#
# Progammer: Joseph Zeko z1797401
#
# Purpose:   This program reads files for france map then 
#           then uses bfs, dfs, dfid to search the map
#




#city_string
#takes a list of nodes called node_list
#formats the list as a string and returns it
def city_string(node_list):
    base_city_string = " ".join([node.name for node in node_list])
    full_city_string = "(" + base_city_string + ")"
    return full_city_string

#city_string_number
#takes a list of nodes called node_list
#formats the list as a string with depth attached and returns it
def city_string_nubmer(node_list):
    base_city_string = ""
    for node in node_list:
        base_city_string += "(" + node.name + " "  + str(node.f) + ")" + " "
    full_city_string = "(" + base_city_string + ")"
    return full_city_string

#bfs
#performs a breadth-first-search
#Variables:
#           from_city - the starting node
#           to_city - the ending node
#           france_roads - the dict of dict for the map of france
def bfs(from_city, to_city, france_roads):

    #declaring variables
    found_path = False
    open_list = [from_city]
    closed_list = []
    name_list = []
    closed_list_name = []
    nodes_expanded = 0

    #while open list is not empty
    while len(open_list)!=0:
        current_node = open_list.pop(0)
        if current_node.name not in closed_list:    #check to see if we've already done this node, just in case
            print("Expanding", current_node.name)

            #check if we succseeded in finding the city
            if current_node.name == to_city.name:
                found_path = True
                break

            #get the children of the current node and sort them
            children = [Node(name, current_node.name) for name in france_roads[current_node.name].keys()]
            children = sorted(children, key=lambda x: x.name)
            print("Children are " + city_string(children))

            #append the node to the closed list
            closed_list.append(current_node)
            closed_list_name.append(current_node.name)
            #check if children are new or not
            new_children = [road for road in children if road not in open_list and road.name not in closed_list_name]
            print("New children are " + city_string(new_children))

            #iterate the nodes_expanded
            nodes_expanded += 1
            for node in open_list:
                name_list.append(node.name)
            
            for node in new_children:                 #for each node in new_children
                if node.name not in closed_list_name:  #if the name is not in closed_list
                    if node.name not in name_list:     #and the name is not in the open name list
                        open_list.append(node)         #append it
            
            #print the open list and closed list
            print("Open list is " + city_string(open_list))
            print("Closed list is " + "(" + " ".join([name for name in closed_list_name]) + ")")
            print("\n")
    #End of loop

    if found_path:
        path_list = []
        print("\n\n")
        while current_node.parent != None:            #while the current node has a parent
            path_list.insert(0,current_node.name)     #insert the current node into the final list
            for node in closed_list:
                if node.name == current_node.parent:  #find current_nodes parent in the list
                    current_node = node               #current_node is now parent
                    break
        path_list.insert(0,current_node.name)         #insert the starting node
        print("Breadth-first search solution:"+ "(" + " ".join([name for name in path_list]) + ")")
        print(str(nodes_expanded) + " nodes expanded")


#dfs
#performs a depth-first-search
#Variables:
#           from_city - the starting node
#           to_city - the ending node
#           france_roads - the dict of dict for the map of france
#           isDFID - a bool that checks if its dfid call or not
#           maxDepth - the maxDepth this should go
def dfs(from_city, to_city, france_roads, isDFID, maxDepth):
    found_path = False
    open_list = [from_city]
    closed_list = []
    nodes_expanded = 0
    name_list = []
    closed_name_list = []
    current_depth = 0
    

    if isDFID is False:          #if its not a dfid call
        maxDepth = float('inf')  #set the maxdepth to infity
    #while open_list is not empty
    while len(open_list)!=0:
        current_node = open_list.pop(0)   #current_node is the front node
        if current_node.name not in closed_name_list:  #check to see if we've already done this node, just in case
            if current_node.f > maxDepth:              #check if current node is past the max depth
                continue                               #skip this loops
            print("Expanding " + current_node.name)
        
            if current_node.name == to_city.name:  #check to see if were on the right node
                found_path = True
                break

            if current_node.f != maxDepth:        #if node is not the maxDepth yet
                #create a node for each of the children with f representing the depth
                children = [Node(name, current_node.name, current_node.f+1) for name in france_roads[current_node.name].keys()]
                children = sorted(children, key=lambda x: x.name)
                
                if isDFID:
                    print("Children are " + city_string_nubmer(children))
                else:
                    print("Children are " + city_string(children))

                #Append the current node to the closed list
                closed_list.append(current_node)
                closed_name_list.append(current_node.name)

                #Checking if the new children need to overrite any of the old nodes
                if isDFID:
                    for node in children:
                        for closednode in closed_list:
                            if closednode.name == node.name:
                                if closednode.f > node.f:
                                    closed_list.remove(closednode)
                                    closed_name_list.remove(closednode.name)
                                    print("* Dropping " + closednode.name + " " + str(closednode.f) + " becuase value is better")


                #Checking if the children are new or not
                new_children = [road for road in children if road not in open_list and road.name not in closed_name_list]
                new_children = sorted(children, key=lambda x: x.name)
                if isDFID:
                    print("New children are " + city_string_nubmer(new_children))
                else:
                    print("New children are " + city_string(new_children))
                
                #append the node to the name list
                for node in open_list:
                    name_list.append(node.name)
                nodes_expanded +=1        #count the nodes
                new_children.reverse()    #reverse the child list so it inserts the correct way
                for node in new_children:
                    if node.name not in closed_name_list:
                        if node.name not in name_list:
                            open_list.insert(0,node)     #insert the new node into the front of the list
                #printing the the open and closed list, depending if its dfid or not
                if isDFID:
                    print("Open list is" + city_string_nubmer(open_list))
                    print("Closed list is "+  city_string_nubmer(closed_list) + "\n")
                else:
                    print("Open list is" + city_string(open_list))
                    print("Closed list is " + city_string(closed_list) + "\n")
            #this is ran if a node is still in the open_list but already at the max depth
            else:
                closed_list.append(current_node)
                closed_name_list.append(current_node.name)
                print("Depth has been reached")
                print("Open list is" + city_string_nubmer(open_list))
                print("Closed list is " + city_string_nubmer(closed_list) + "\n")
    #end of loop

    if found_path:
        path_list = []
        print("\n\n")
        #Finds the complete path for the algorithm
        #same as the breadth-first one
        while current_node.parent != None:
            path_list.insert(0,current_node.name)
            for node in closed_list:
                if node.name == current_node.parent:
                    current_node = node
                    break
        path_list.insert(0,current_node.name)

        #prints the solution and the expanded nodes
        if not isDFID:
            print("Depth-first search solution:"+ "(" + " ".join([name for name in path_list]) + ")")
            print(str(nodes_expanded) + " nodes expanded")
        else:
            print("DFID solution:"+ "(" + " ".join([name for name in path_list]) + ")")
            print(str(nodes_expanded) + " nodes expanded")
            return True

#dfid
#performs a depth-first-iterative-deepening
#Variables:
#           from_city - the starting node
#           to_city - the ending node
#           france_roads - the dict of dict for the map of france
#           maxDepth - the maxDepth this should go
def dfid(from_city, to_city, france_roads, maxDepth):
    counter = 0                #counter for depth
    found_target = False
    while int(maxDepth) >= counter:  #while maxDepth is greater then counter
        print("\nDFID LEVEL " + str(counter) + ":\n")      #print the level
        found_target = dfs(from_city,to_city, france_roads,True,counter) #call  the dfs fucntion
        if found_target:       #if dfs found the target break out of loop
            break
        counter += 1    #go one deeper
    if not found_target:
        print("DFID Failed to find target")

#error checking for command line arguments
if len(sys.argv) < 3:
    print("Not enough command line arguments")
    quit(1)
if sys.argv[1] not in outer_dict.keys():
    print("Argument 1 is not in the map")
    quit(1)
if sys.argv[2] not in outer_dict.keys():
    print("Argument 2 is not in the map")
    quit(1)
if not sys.argv[3].isdigit():
    print("Argument 3 must be nubmer")
    quit(1)

#getting the command line arguments
from_city = sys.argv[1]
to_city = sys.argv[2]
maxDepth = sys.argv[3]

#Call the functions
print("\n\nStaring BFS\n")
bfs(Node(from_city), Node(to_city), outer_dict)
print("\n\nStaring DFS\n")
dfs(Node(from_city), Node(to_city), outer_dict, False, 0)
print("\n\nStaring DFID\n")
dfid(Node(from_city), Node(to_city), outer_dict,maxDepth)