
def heurisitic(x1,y1,x2,y2): #Manhattan Distance
    print(x1)
    print(type(x1))
    return abs(int(x1)-int(x2))+abs(int(y1)-int(y2))

graph={'(A)': {'g(n)':17, '(0,2)':2, '(0,3)':3}, #assume this is a start node 
           '(B)': {'g(n)':4, '(5,4)':5},    #assume this is the goal node

}


l_keys = list(graph.keys())
l_values=graph.values()
#l_values_values=list(l_values.values())

#print(type(heurisitic(l_keys[0][1],l_keys[0][3], l_keys[1][1], l_keys[1][3])))

#def minimum(graph):

'''
for i,j in graph.items():
    print(min(j.values()))
    for i in j:
        if (min(i.values())):
            print(i)
   
'''
for i in l_values:
    print (min(i.values()))
print(min(graph, key=lambda k:float(graph[k]['g(n)'])))

#print(graph['(0,1)'])

#unvisited ={'(0,1)': g(), f(), nn}

neigh= '(0,1)'

#def get_params(neigh): 
print(neigh[1])




