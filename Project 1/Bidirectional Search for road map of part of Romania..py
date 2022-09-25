class Node:
    def __init__(self, CityName, NodeNum):
        self.NodeNum = NodeNum
        self.CityName = CityName
        self.next = None

class GraphTree:
    def __init__(self, TotalNumNodes):
        self.TotalNumNodes = TotalNumNodes
        self.graphTree = [None] * self.TotalNumNodes
        self.SourceQueue = list()
        self.DestinationQueue = list()

        self.SourceNodeVisited = [False] * self.TotalNumNodes
        self.DestinationNodeVisisted = [False] * self.TotalNumNodes

        self.ParentSourceNodes = [None] * self.TotalNumNodes
        self.ParentDestinationNodes = [None] * self.TotalNumNodes

    def Connect(self, source, destination):
        node = Node(destination[0], destination[1])
        node.next = self.graphTree[source[1]]
        self.graphTree[source[1]] = node

        node = Node(source[0], source[1])
        node.next = self.graphTree[destination[1]]
        self.graphTree[destination[1]] = node


class BidirectionalSearch:
    def __init__(self, graphTree):
        self.TotalNumNodes = len(graphTree.graphTree)
        self.graphTree = graphTree.graphTree
        self.SourceQueue = list()
        self.DestinationQueue = list()

        self.SourceNodeVisited = [False] * self.TotalNumNodes
        self.DestinationNodeVisisted = [False] * self.TotalNumNodes

        self.ParentSourceNodes = [None] * self.TotalNumNodes
        self.ParentDestinationNodes = [None] * self.TotalNumNodes

        ########################################################
        self.Cities_names = ['Ordea','Zerind','Arad','Timisoara','Lugoj','Mehadia','Drobeta','Craiova','Rimnicu Vilcea','Sibiu','Fagaras','Pitesti','Giurgiu','Bucharest','Urziceni','Neamt','Iasi','Vaslui','Hirsova','Eforie']

        #########################################################

    def bfs(self, isForward=True):

        if isForward:

            # BFS in forward direction
            current = self.SourceQueue.pop(0)
            connected_node = self.graphTree[current]

            while connected_node:
                node = connected_node.NodeNum

                if not self.SourceNodeVisited[node]:
                    self.SourceQueue.append(node)
                    self.SourceNodeVisited[node] = True
                    self.ParentSourceNodes[node] = current

                connected_node = connected_node.next
        else:

            # BFS in backward direction
            current = self.DestinationQueue.pop(0)
            connected_node = self.graphTree[current]

            while connected_node:
                node = connected_node.NodeNum

                if not self.DestinationNodeVisisted[node]:
                    self.DestinationQueue.append(node)
                    self.DestinationNodeVisisted[node] = True
                    self.ParentDestinationNodes[node] = current

                connected_node = connected_node.next

    def is_intersecting(self):

        # Returns intersecting node
        # if present else -1
        for i in range(self.TotalNumNodes):
            if (self.SourceNodeVisited[i] and
                    self.DestinationNodeVisisted[i]):
                return i

        return -1

    def print_path(self, intersecting_node,
                   src, dest):

        # Print final path from
        # source to destination
        path = list()
        path.append(self.Cities_names[intersecting_node])
        i = intersecting_node

        while i != src:
            path.append(self.Cities_names[self.ParentSourceNodes[i]])
            i = self.ParentSourceNodes[i]

        path = path[::-1]
        i = intersecting_node

        while i != dest:
            path.append(self.Cities_names[self.ParentDestinationNodes[i]])
            i = self.ParentDestinationNodes[i]

        print("*****Path*****")
        path = list(map(str, path))
        print(' --> '.join(path))

    def bidirectional_search(self, src, dest):

        # Add source to queue and mark
        # visited as True and add its
        # parent as -1
        self.SourceQueue.append(src)
        self.SourceNodeVisited[src] = True
        self.ParentSourceNodes[src] = -1

        # Add destination to queue and
        # mark visited as True and add
        # its parent as -1
        self.DestinationQueue.append(dest)
        self.DestinationNodeVisisted[dest] = True
        self.ParentDestinationNodes[dest] = -1

        while self.SourceQueue and self.DestinationQueue:

            # BFS in forward direction from
            # Source Vertex
            self.bfs(True)

            # BFS in reverse direction
            # from Destination Vertex
            self.bfs(False)

            # Check for intersecting vertex
            intersecting_node = self.is_intersecting()

            # If intersecting vertex exists
            # then path from source to
            # destination exists
            if intersecting_node != -1:
                print(f"Path exists between {self.Cities_names[src]} and {self.Cities_names[dest]}")
                print(f"Intersection at : {self.Cities_names[intersecting_node]}")
                self.print_path(intersecting_node,
                                src, dest)
                return 0
        return -1
TotalNumCities = 20
src = 7
dest = 15
# Create graph of Romania
graph = GraphTree(TotalNumCities)
graph.Connect(['Ordea', 0], ['Sibiu', 9])
graph.Connect(['Ordea', 0], ['Zerind', 1])
graph.Connect(['Zerind', 1], ['Arad', 2])
graph.Connect(['Arad', 2], ['Sibiu', 9])
graph.Connect(['Arad', 2], ['Timisoara', 3])
graph.Connect(['Timisoara', 3], ['Lugoj', 4])
graph.Connect(['Lugoj', 4], ['Mehadia', 5])
graph.Connect(['Mehadia', 5], ['Drobeta', 6])
graph.Connect(['Drobeta', 6], ['Craiova', 7])
graph.Connect(['Sibiu', 9], ['Fagaras', 10])
graph.Connect(['Sibiu', 9], ['Rimnicu Vilcea', 8])
graph.Connect(['Rimnicu Vilcea', 8], ['Pitesti', 11])
graph.Connect(['Rimnicu Vilcea', 8], ['Craiova', 7])
graph.Connect(['Craiova', 7], ['Pitesti', 11])
graph.Connect(['Fagaras', 10], ['Bucharest', 13])
graph.Connect(['Pitesti', 11], ['Bucharest', 13])
graph.Connect(['Bucharest', 13], ['Giurgiu', 12])
graph.Connect(['Bucharest', 13], ['Urziceni', 14])
graph.Connect(['Urziceni', 14], ['Hirsova', 18])
graph.Connect(['Hirsova', 18], ['Eforie', 19])
graph.Connect(['Urziceni', 14], ['Vaslui', 17])
graph.Connect(['Vaslui', 17], ['Iasi', 16])
graph.Connect(['Iasi', 16], ['Neamt', 15])

bds = BidirectionalSearch(graph)
out = bds.bidirectional_search(src, dest)

if out == -1:
    print(f"Path does not exist between {GraphTree.graphTree[src].CityName} and {GraphTree.graphTree[dest].CityName}")

