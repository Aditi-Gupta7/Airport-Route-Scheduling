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
            
    return airports, routes, start_airport

airports, routes, start_airport = create_list()