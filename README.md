# Airport-Route-Scheduling

<b><h3>Problem statement:</h3><p>
An airline company wants to know if his flights are servicing all major cities /airports such that if a passenger wants to travel from a given starting city, they can reach any of the other cities using either a direct flight (0 stops) or an indirect flight (multiple stops at intermediate cities). If there are any cities that are not reachable, the airline wants to know the minimum number of flights (one-way flights) that need to be added so that the passenger can reach any destination city from the starting city using either direct or indirect flights. We have a list of city airports (three-letter codes like “JFK”), a list of routes (one-way flights from one airport to another like [“JFK” , “SFO”] ), and a starting city / airport The routes only allow you to fly in one direction; for instance, the route [“JFK”, “SFO”] only allows you to fly from “JFK” to “SFO” and not from SFO to JFK. Also, the connections don’t have to be direct (take off at the starting airport and land in the destination airport). It is okay if the destination airport can be reached from the starting airport by stopping at other intermediary airports in between.


<b><h3>Design:</h3><p>
From an architecture perspective, we would like to reiterate that what we need to find is the minimum number of connections between airports to connect all airports from a given source airport. The best suited data structure to represent all the input airport/cities and their connectivity from flights is Graph. So we will process the input cities/airports and the routes among these airports and store it into a directional graph.

The graph for sample input will come like below:<p>
 <img width="370" alt="1" src="https://user-images.githubusercontent.com/103483074/202207691-d9290f49-d259-4c33-8d17-fbc79bed7d9b.png">

Now in the next step what we want is to find the strongly connected components of this graph. The strongly connected component of a graph is a subgraph of the main graph in which all airports are connected with all other airports of the same strongly connected component. For the above graph, below would be the strongly connected components circled together.<p>
<img width="368" alt="2" src="https://user-images.githubusercontent.com/103483074/202207895-c394ffbc-4f9c-46a1-bdad-c127636a0c8d.png">
 
In the next step we will create a compressed graph. The compressed graph will have the compressed node for the strongly connected components. Compressed node can be visualized as a node which will have the subgraph which is strongly connected. After applying this step our compressed graph will look like below: <p>
<img width="367" alt="3" src="https://user-images.githubusercontent.com/103483074/202208004-178ef069-0737-44a7-9c9e-f29ca766ba15.png">

Now we need to find all nodes in the compressed graph which will have zero incoming edge. Below is the graph with the number of incoming edges in the above compressed graph. <p>
<img width="365" alt="4" src="https://user-images.githubusercontent.com/103483074/202208072-c852679d-bc0c-4bb4-8e97-1a3100bf13d9.png">

Now we need to connect the source Airport LGA to all nodes which have zero incoming edges. 

For a compressed node, we can choose any node within the strongly connected component of that compressed node.<p>
<img width="368" alt="5" src="https://user-images.githubusercontent.com/103483074/202208173-851159b8-c9e9-49bd-8280-3fd1c7fe3ffc.png">
<p>So, the required routes are LGA - EWR, LGA - TLV and LGA - EYW

Finding strongly connected components & Compressed node:<p>
For finding strongly connected components of the graph, we have used the Kosaraju algorithm, which uses DFS on the edge list and reverse of the edge list to find the strongly connected components. First, we do DSF on the route edge list and create a stack and then we do DSF on the reverse of the route edge list to find the subgraph which has a loop and hence is strongly connected.
While DFS on the reverse of the route edge list, we also created the compressed node for each strongly connected component. We have given the first node of the strongly connected component as its representative node.

<b><h3>Summary:</h3><p>
The approach can be summarized as follows:
1. Modify the input into readable format
	a) Give all the airports an ID
	b) Convert routes into adjacency matrix for each airport ID
	-Replace routes with their IDs in route list
c) Convert starting airport to ID format

2. Apply Kosaraju Algorithm to find SCCs
	a) Perform DFS traversal of the graph, and push nodes to stack before back tracking.
	b) Change the edge directions of the graph using transpose
	c) Pop elements from stack and perform dfs for that element on reverse graph

3. Replace the strongly connected components with a representative node

4. Find the in-degree of all the representative nodes.

5. When node != starting node, and in-degree is 0, add a flight to that node from the starting airport
