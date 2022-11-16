#Read the input file line by line and create a list of airports and routes
def create_list():
    inp_file = open(r'C:\Users\aditi\Documents\Assignments\DSAD\1\AirportConnections\input.txt')
    all_lines = inp_file.readlines()
    routes = []
    for line in all_lines:      

        # Create list for airport codes like  ['CNH', 'DLE', 'WBL' 'MGE'] 
        if line.startswith('airports'):
            airports_input = line[11:].strip()
            airports = airports_input.split(",")
            for x in range(len(airports)):
                if airports[x].startswith(' '):
                    airports[x] = airports[x][1:]
        
        # Create list for routes like [['CNH', 'DLE'], ['CNH', 'MUD'], ['DLE', 'KLO']]
        elif not(line.startswith('routes')) and not(line.startswith('airports')) and not(line.startswith('Starting Airport')):
            stripped_line = line.replace(" ", "")
            line_list = stripped_line.split(',')
            line_list = line_list[:2]
            routes.append(line_list)
        
        # Get the starting airport like DLE
        elif line.startswith('Starting Airport'):
            start_airport = line[-3:].strip()

    # print("airports", airports)
    # print("Routes: ",routes)
    # print("Start_ airport: " , start_airport)       
    return airports, routes, start_airport

def get_airport_id(noof_airports):
    for i in range(noof_airports):
        airport_ids[airports[i]] = i
    # print("AIRPORT DICTIONARY = ",airport_ids)
    return airport_ids

def get_route_matrix(noof_airports):
    route_matrix = [[0 for i in range(noof_airports)] for j in range(noof_airports)]
    # print(route_matrix)
    for i in range(len(routes)):
        for j in range(2):
            id = airport_ids[routes[i][j]] #Get airport ids for each route
            if j == 0:
                start = id
            elif j == 1:
                dest = id 
        route_matrix[start][dest]  = 1
    return route_matrix

def dfs(i, vis, KR_stack):
    vis[i] = True
    for j in range(length_route_matrix):
        if route_matrix[i][j] == 1 and vis[j] == False:
            dfs(j, vis, KR_stack)
    KR_stack.append(i)

def get_reverse_route_matrix(noof_airports):
    reverse_route_matrix = [[0 for i in range(noof_airports)] for j in range(noof_airports)]
    for i in range(length_route_matrix):
        for j in range(length_route_matrix):
            reverse_route_matrix[i][j] = route_matrix[j][i]
    return reverse_route_matrix

def dfs_and_representative_node(node, representative, vis, rep, reverse_route_matrix):
    vis[node] = True
    rep[node] = representative
    for j in range(length_route_matrix):
        if reverse_route_matrix[node][j] == 1 and vis[j] == False:
            dfs_and_representative_node(j, representative, vis, rep, reverse_route_matrix)
    return rep

def KR_algo(length_route_matrix, rep):
    vis = [False] * length_route_matrix
    KR_stack = []
    # 1. Perform DFS traversal of the graph, and push nodes to stack before back tracking
    for i in range(length_route_matrix):
        if vis[i] == False:
            dfs(i, vis, KR_stack)

    # 2. Change the edge directions of the graph using transpose
    reverse_route_matrix = get_reverse_route_matrix(noof_airports)
    # print(reverse_route_matrix)

    # 3. Pop elemens from stack and perform dfs for that element on reverse graph and create a compressed graph
    vis = [False] * length_route_matrix
    for i in range(len(KR_stack)-1, -1, -1):
        node = KR_stack[i]
        KR_stack.pop(i)
        if vis[node] == False:
            dfs_and_representative_node(node, node, vis, rep, reverse_route_matrix)

def initialize_in_degree():
    # Make in-degree of all the rep nodes as 0 and non-rep nodes as -1
    in_deg = [-1] * length_route_matrix
    for i in range(length_route_matrix):
        if rep[i] == i:
                in_deg[i] = 0
    return in_deg

def find_in_degree(in_deg):
    # Find the in-degree of the nodes
    for i in range(length_route_matrix):
        for j in range(length_route_matrix):
            if route_matrix[j][i] == 1 and rep[i] != rep[j]:
                in_deg[rep[i]] = in_deg[rep[i]] + 1
    return in_deg
  
def flights_to_be_added():
    noof_flights = 0
    destination = []
    for i in range(len(in_deg)):
        if in_deg[i] == 0 and i!=start_airport_id:
            dest = list(airport_ids.keys())[list(airport_ids.values()).index(i)]
            destination.append(dest)
            noof_flights = noof_flights + 1
    return noof_flights,destination

if __name__ == "__main__":
    airports, routes, start_airport = create_list() #Get list of airports, routes, start_airport
    noof_airports = len(airports)
    airport_ids = {} # Assign an ID to each airport
    get_airport_id(noof_airports)
    start_airport_id = airport_ids[start_airport]

    # Get the adacency matrix for all the routes
    route_matrix = get_route_matrix(noof_airports)

    # Apply Kosaraju algorith to identify strongly connected components
    length_route_matrix = len(route_matrix)
    rep = [-1]*length_route_matrix
    # vis = [False] * length_route_matrix
    KR_algo(length_route_matrix, rep)

    # Find nodes with in-degree = 0 and then find no. of flights to be added
    in_deg = initialize_in_degree()
    in_deg = find_in_degree(in_deg)
    noof_flights,destination = flights_to_be_added()
    print(noof_flights)
    for i in destination:
        print(start_airport,i)