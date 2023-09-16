#Splitting the input list into 2 seperate list of top and bottom
def topBottom(lst):
    bottom=[]
    top=[]

    #looping through the list and seperating top from bottom
    for i in lst:
        top += [i[0]]
        bottom +=[i[1]]

    return [top,bottom]

def pcp_bfs(lst):
    top= topBottom(lst)[0] #list of strings on the top
    bottom= topBottom(lst)[1] #list of strings on the bottom
    top_fringe=[top[0]]
    bottom_fringe=[bottom[0]]
    loop=True

   
    while loop:
        if top_fringe==[] or bottom_fringe==[]:
            print("No Solution")
            loop= False
        else:
            top_node= top_fringe[0]
            bottom_node= bottom_fringe[0]
            print("Top Node being checked: ", top_node)
            print("Bottom Node being checked: ", bottom_node)
            top_fringe.pop(0)
            bottom_fringe.pop(0)
            

            if top_node == bottom_node:
                print( "Solution is: ", top_node)
                loop= False
            else:
                for i in range (0,len(top)):       
                    top_fringe += [top_node+ top[i]]
                    bottom_fringe += [bottom_node+ bottom[i]]

                    
                    
                   
                    
    


            




    


lst=[("MOM","M"), ("O", "OMOMO")]
pcp_bfs(lst)