# import os
# absolute_path = os.path.dirname(__file__)

#To read input file and create airport and route list
def create_list():
    # inp_file = open('inputPS12.txt')
    inp_file = open(r'C:\Users\aditi\Documents\Assignments\DSAD\1\AirportConnections\inputPS12.txt')
    all_lines = inp_file.readlines()
    routes = []
    for line in all_lines:
        if line.startswith('airports'):         #create list for airport codes
            airports_input = line[11:].strip()
            airports = airports_input.split(",")
            for x in range(len(airports)):
                if airports[x].startswith(' '):
                    airports[x] = airports[x][1:]
            #print(airports)
        
        elif(line != "routes\n" and line[0:8] != "airports" and line[0:8] != "Starting"):  #create list for routes
            stripped_line = line.strip()
            line_list = stripped_line.split(",")
            if len(line_list) > 2:
                line_list = line_list[:2]
            if line_list[1].startswith(' '):
                line_list[1] = line_list[1][1:]
            routes.append(line_list)
        
        elif line.startswith('Starting Airport'):
            start_airport = line.strip()[-3:len(line)]
            
    return airports, routes, start_airport

#To perform DFS and find the stack
def dfs1(i):
    vis[i] = True
    for j in range(n):
        if route_matrix[i][j] == 1:
            if (vis[j] == False) :
                dfs1(j)
    stack.append(i)

#To perform the DFS, after the stack is full
def dfs2(u, representative):
    vis2[u] = True
    who[u] = representative
    for j in range(n):
        if route_matrix_reverse[u][j] == 1:
            if (vis2[j] == False) :
                dfs2(j,representative)

#Call this function to find the minimum number of one-way flights, that needs to be added so that 
#the passenger can reach any destination city from the starting city using either direct or indirect flights.  
def min_flights(airports, routes, start_airport):
    airport_id = []
    start_airport_id = -1
    
    #Loop to give each airport name, an ID
    for i in range(n):
        if airports[i] == start_airport:
            start_airport_id = i
        airport_id.append([airports[i],i])
    #print("The airport ids are:", airport_id)
   
    #Loop to create adjacency matrix of routes
    for i in range(len(routes)):
        for j in range(2):
            for k in range(n):
                if(routes[i][j] == airport_id[k][0]):
                    if j == 0:
                        a = airport_id[k][1]
                    else:
                        b = airport_id[k][1]
        route_matrix[a][b]  = 1
    #print(route_matrix)
    
    #Find the strongly connected components(SCC) in the graph
    #Function to travesre the graph using DFS
    for i in range(n):
        if(vis[i] == False):    #If the nod has not been visites, perfom DFS on that node
            dfs1(i)
    #print("Stack is:", stack)
    
    #Transpose of the route matrix
    for i in range(n):
        for j in range(n):
            route_matrix_reverse[i][j] =  route_matrix[j][i]
    #print(route_matrix_reverse)
    
    #Find the representative node of each original node, that belongs to the same strongly connected component
    for i in range((n-1),-1,-1):
        u = stack[i]
        stack.pop(i)
        if vis2[u] == False:
            dfs2(u,u)
    #print("Who array:", who)
    
    #Capture the in-degree of the compressed nodes (Representative node of the SCC)
    for i in range(n):
        for j in range(n):
            if (route_matrix[i][j] == 1) and (who[i] != who[j]):
                #in_deg[j] = in_deg[j]+1
                in_deg[who[j]] = in_deg[who[j]]+1
    #print("In-degree:",in_deg)
    
    ans=0
    dest=[]
    #Capture the representative nodes, with in-degree of 0 (which are not the strating node)
    for i in range(n):
            if (in_deg[i] == 0) and (who[i] == i) and (i != who[start_airport_id]):
                dest.append(airports[i])
                ans = ans+1
                
    with open('outputPS12.txt', 'w') as output_file:
        output_file.write("The minimum flights that need to be added = ")
        output_file.write(str(ans))
        output_file.write("\nThe flights that need to be added are:")
        for i in range(len(dest)):
            output_file.write("\n["+start_airport)
            output_file.write(", "+dest[i]+"]")

if __name__ == "__main__":
    airports, routes, start_airport = create_list() #Read input file and create list
    n = len(airports)
    route_matrix = [[0 for col in range(n)] for row in range(n)]    #To record all the edges
    # route_matrix_reverse = [[0 for col in range(n)] for row in range(n)]    #To record the reverse edges
    # vis = [False] * n   #Keep track of the visited nodes in dfs1
    # vis2 = [False] * n  #Keep track of the visited nodes in dfs2
    # stack = []
    # who = [-1] * n      #To capture the node, which represents the strongly connected components
    # in_deg = [0] * n    #To capure the in-degree of the strongly connected components
    # min_flights(airports, routes, start_airport)