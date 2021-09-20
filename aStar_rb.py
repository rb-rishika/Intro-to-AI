infinity = float('infinity')

def heurisitic(x1,y1,x2,y2): #Manhattan Distance
	return abs(int(x1)-int(x2))+abs(int(y1)-int(y2))
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
	G_score=0
	F_score=1
	Previous=2

	visited ={}    #empty dictionaries
	unvisited={}   #nested dictionaries

	for key in graph:
		unvisited[key]=[infinity , infinity , None]   #(f(n, g(n).parent node))
	print(unvisited) #end of for 

	h_score = heurisitic(l_keys[0][1],l_keys[0][3], l_keys[23][1], l_keys[23][3])
	print(h_score)

	unvisited[start_node] = [0, h_score, NULL]  
	finished = False

	#ASTAR START
	While (finished == False):
		if(len(unvisited)==0):
			finished= True
		else:
			



astar(graph, '(0,0)', '(3,7)')
