import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = np.arange(0, 8).tolist()  # Fixed np.arange

G.add_nodes_from(nodes)

# Add edges
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (2, 7)]
G.add_edges_from(edges)

# Define positions
pos = {
    0: (10, 10),
    1: (7.5, 7.5),
    2: (12.5, 7.5),
    3: (6, 6),
    4: (9, 6),
    5: (11, 6),
    6: (14, 6),  
    7: (17, 6)
}

# Define labels
labels = {
    0: "CEO",
    1: "Head of Marketing",
    2: "Head of Sales",
    3: "Marketing Manager",
    4: "Marketing Manager",
    5: "Sales Manager",
    6: "Sales Manager",
    7: "Sales Manager"
}

# Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, labels=labels, arrows=True,
                 node_shape="s", node_size=10000, node_color="skyblue",
                 font_size=10, font_weight="bold", edge_color="gray")

# Display the chart
plt.title("Organization Chart")
plt.show()
