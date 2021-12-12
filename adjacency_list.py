#  A weighted adjacency list will be used to store nodes and their distances to each other.

class AdjacencyList:
    adjacency_list = {}
    node_list = []

    def add_node(self, node):
        if node not in self.node_list:
            self.node_list.append(node)
        else:
            print("Node ", node , " already exists!")

    def add_edge(self, node1, node2, weight):
        temp = []
        if node1 in self.node_list and node2 in self.node_list:
            if node1 not in self.adjacency_list:
                temp.append([node2, weight])
                self.adjacency_list[node1] = temp

            elif node1 in self.adjacency_list:
                temp.extend(self.adjacency_list[node1])
                temp.append([node2, weight])
                self.adjacency_list[node1] = temp

        else:
            print("These nodes don't exist")

    def print_graph(self):
        for node in self.adjacency_list:
            print(node, "---> ", [i for i in self.adjacency_list[node]])


# Create an adjacency list and add some test nodes and edges
test_list = AdjacencyList()
test_list.add_node(0)
test_list.add_node(1)
test_list.add_node(2)
test_list.add_node(3)
test_list.add_node(4)
test_list.add_edge(0,1,2)
test_list.add_edge(1,2,2)
test_list.add_edge(2,3,4)
test_list.add_edge(2,4,3)
test_list.add_edge(3,0,5)
test_list.add_edge(3,4,3)
test_list.add_edge(4,0,1)

test_list.print_graph()

print(test_list.adjacency_list)

