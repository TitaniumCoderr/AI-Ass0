#first in FIFO data structure
def bfs_geography(lst):

    node=[lst[0]]
    fringe=[node]
    loop=True
   
    while loop:
        storage=[] #location to store words with the same initial letter
        if fringe==[]:
            print("No Solution")
            loop= False
        else:
            node = fringe[0]#first element from the frindge is new node
            print("Node getting checked ", node)
            fringe.pop(0) #remove the first element from the frindge
            
            if goal(node,lst):
                print("SOLUTION IS: ", node)  
                loop=False
  
            bfs_successor(lst,storage,node,fringe)

            
        
#Successor Function
def bfs_successor(lst,storage,node,fringe):
   #Searching the input list for potential paths and adding them to a "storage"
   for i in lst:
       if node[-1][-1]== i[0]:
           storage += [i]
   #looping through the storage 
   for i in storage:
       if i not in node: #checking is element in storage is already in the node. Eliminates repitition
           fringe+=[node+[i]] # adding the new path/node to the  back of the fringe
   print("Updated Fringe: ", fringe)
   print("")

#Goal Function
def goal(node,lst):
    #Checking if the node is the goal state
    if len(node)==len(lst):
        return True
    return False        
        
lst=['ABC', 'CDE', 'CFG', 'EHE', 'EIJ', 'GHK','GLC']
#lst=['ABC', 'CDE', 'CFG', 'EHI', 'GJC', 'GKG']
bfs_geography(lst)
