
import networkx as nx
import matplotlib.pyplot as plt


# Implementation of welsh_powell algorithm
def welsh_powell(G):
    # Sorting the nodes based on their degree (valency) in descending order
    node_list = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    col_val = {}  # dictionary to store the colors assigned to each node
    col_val[node_list[0]] = 0  # assign the first color to the first node
    
    # Assign colors to remaining N-1 nodes
    for node in node_list[1:]:
        available = [True] * len(G.nodes())  # boolean list[i] contains false if the node color 'i' is not available

        # Iterates through all the adjacent nodes and marks its color as unavailable, if its color has been set already
        for adj_node in G.neighbors(node): 
            if adj_node in col_val.keys():
                col = col_val[adj_node]
                available[col] = False
        
        clr = 0
        for clr in range(len(available)):
            if available[clr] == True:
                break
        col_val[node] = clr
    
    print(col_val)
    return col_val


# Takes input from the file and creates an undirected graph
def CreateGraph():
    G = nx.Graph()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        for i in range(n):
            graph_edge_list = f.readline().split()
            G.add_edge(graph_edge_list[0], graph_edge_list[1]) 
    return G


# Draws the graph and displays the colors on the nodes
def DrawGraph(G, col_val):
    pos = nx.spring_layout(G)
    # Create a color map for better visualization
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']
    node_colors = [colors[col_val.get(node, 0) % len(colors)] for node in G.nodes()]
    
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='black', width=1, alpha=0.7)
    
    # Add a legend showing the color assignments
    legend_elements = []
    for node, color_idx in col_val.items():
        color = colors[color_idx % len(colors)]
        legend_elements.append(f"Node {node}: Color {color_idx}")
    
    plt.title("Graph Coloring using Welsh-Powell Algorithm")
    print(f"Number of colors used: {max(col_val.values()) + 1}")


# Main function
if __name__ == "__main__":
    G = CreateGraph()
    col_val = welsh_powell(G)
    DrawGraph(G, col_val)
    plt.show()