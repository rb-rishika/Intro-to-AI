infinity = float('infinity')

def get_minimum (unvisited):
	return min(unvisited, key=lambda k:float(unvisited[k][0]))

def heurisitic(x1,y1,x2,y2): #Manhattan Distance
	return abs(int(x1)-int(x2))+abs(int(y1)-int(y2))

def get_params(curr, neigh): 
	x1=curr[1]
	y1=curr[3]
	x2=neigh[1]
	y2=neigh[3]
	return x1,y1,x2,y2

#nested dicts
graph = {   #g(n)
		   '(0,0)': {'(0,1)':10, '(1,0)':12},
		   '(0,1)': {'(0,0)':10, '(1,1)':11, '(0,2)':10},
		   '(0,2)': {'(0,1)':12, '(1,2)':6, '(0,3)':8},
		   '(0,3)': {'(0,2)':6, '(1,3)':5, '(0,4)':6},
		   '(0,4)': {'(0,3)':11},
		   '(0,6)':{'(0,7)':9}, 
		   '(0,7)':{'(1,7)':9}, 
		   '(1,0)':{'(1,1)':10, '(2,0)':3},
		   '(1,1)':{'(1,0)':3,'(0,1)':8, '(1,2)':9},
		   '(1,2)':{'(1,1)':5, '(0,2)':8, '(1,3)':4},
		   '(1,3)':{'(0,3)':6, '(1,2)':5 , '(2,3)':7},
		   '(1,7)':{'(0,7)':5, '(2,7)':5},
		   '(2,0)':{'(1,0)':2, '(3,0)':15},
		   '(2,3)':{'(1,3)':2, '(2,4)':5, '(3,3)':6},
		   '(2,4)':{'(2,3)':6, '(3,4)':1},
		   '(2,6)':{'(3,6)':5, '(2,7)':5},
		   '(2,7)':{'(1,7)':2, '(2,6)':3},
		   '(3,0)':{'(2,0)':7, '(3,1)':5},
		   '(3,1)':{'(3,0)':7},
		   '(3,3)':{'(2,3)':7, '(3,4)':5},
		   '(3,4)':{'(3,3)':1, '(2,4)':5,'(3,5)':8},
		   '(3,5)':{'(3,4)':6, '(3,6)':5},
		   '(3,6)':{'(3,5)':1, '(2,6)':5},
		   '(3,7)':{'(3,6)':7, '(2,7)':4}
		 }
print(graph)
start_node='(0,0)'
target_node='(3,7)'

def astar(graph, start_node, target_node): 
	l_keys = list(graph.keys())
	G_SCORE=0
	F_SCORE=1
	PREVIOUS=2

	visited ={}    #empty dictionaries
	unvisited={}   #nested dictionaries

	for key in graph:
		unvisited[key]=[infinity , infinity , None]   #(g(n), f(n), parent node)), copying entire graph in unvisited 

	h_score = heurisitic(l_keys[0][1],l_keys[0][3], l_keys[23][1], l_keys[23][3])
	print(h_score)

	unvisited[start_node] = [0, h_score, None]  
	print (unvisited)
	finished = False

	#ASTAR START
	while (finished == False):
		if(len(unvisited)==0):
			finished= True
		else:
			current_node=get_minimum(unvisited)
			if (current_node==target_node):
				finished=True
				visited[current_node] = unvisited[current_node]   #End of if
			else: 
				for neigh in graph[current_node]:
					#we will check only UNVISITED NODES
					if neigh not in visited:     # Calculate new g-score
						new_g_score = unvisited[current_node][G_SCORE] + graph[current_node][neigh]
						if new_g_score < unvisited[neigh][G_SCORE]: 
							#updation 
							unvisited[neigh][G_SCORE] = new_g_score
							x1,y1,x2,y2=get_params(current_node, neigh)
							unvisited[neigh][F_SCORE] = new_g_score + heurisitic(x1,y1,x2,y2)
							unvisited[neigh][PREVIOUS] = current_node #end of inner if 
							#end of outer if
				visited[current_node] = unvisited[current_node] 		# Add current node to visited list
				del unvisited[current_node]
		                # Remove from unvisited list
	return visited

#end of astar function 
astar(graph, '(0,0)', '(3,7)')
