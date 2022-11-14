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

def get_airport_id():
    for i in range(len(airports)):
        airport_ids[airports[i]] = i
    # print("AIRPORT DICTIONARY = ",airport_ids)
    return airport_ids

def get_route_matrix():
    route_matrix = [[0 for i in range(len(airports))] for j in range(len(airports))]
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



airports, routes, start_airport = create_list()
airport_ids = {}
get_airport_id()
route_matrix = get_route_matrix()
