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

#Airport IDs
def get_airport_id():
    for i in range(len(airports)):
        airport_ids.append([airports[i],i])
    # print(airport_ids)
    return airport_ids


airports, routes, start_airport = create_list()

airport_ids = []
get_airport_id()

route_ids = routes.copy()

for i in airport_ids:
    airport_name = i[0]
    airport_id = i[1]
    for i in routes:
        if routes[0] == airport_name:
            route_ids[]


