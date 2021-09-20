
def heurisitic(x1,y1,x2,y2): #Manhattan Distance
    print(x1)
    print(type(x1))
    return abs(int(x1)-int(x2))+abs(int(y1)-int(y2))

graph={'(0,0)': {'(0,1)':1, '(0,2)':2, '(0,3)':3}, #assume this is a start node 
           '(0,1)': {'(0,3)':4, '(5,4)':5},    #assume this is the goal node

}


l_keys = list(graph.keys())
l_values=list(graph.values())
#l_values_values=list(l_values.values())

#print(type(heurisitic(l_keys[0][1],l_keys[0][3], l_keys[1][1], l_keys[1][3])))

#def minimum(graph):

for j in l_values:
    print(min(j.values())
    #if(j.values()==min):
        #print(l_values.key())
'''
    print(j.keys(), min(j.values()))
    if(min<min())'''
    #res = [key for j in l_values if l_values[j] == min]
    #print(res)


    '''
    for k in j:
        print(j[k])
    #print(l_values[i][2])
  '''
