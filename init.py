import igraph as ig
import networkx as nx
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

NODES = [
    "LOGIN",
    "ACCOUNT A",
    "ACCOUNT B",
    "ACCOUNT CUSTOMER FACING",
    "ACCOUNT DATA FACING"
]


USER_1_1 = [
    ["LOGIN", "ACCOUNT A"],
    ["ACCOUNT A", "ACCOUNT B"],
    ["ACCOUNT B", "ACCOUNT CUSTOMER FACING"],
    ["ACCOUNT B", "ACCOUNT DATA FACING"],
]

# user_journey = ig.Graph(
#     edges=USER_1_1,
# )
user_journey = nx.Graph()
user_journey.add_nodes_from(NODES)
# user_journey.add_edges_from([USER_1_1[0]])
# pos = nx.spring_layout(user_journey)

# plt.figure()
# nx.draw(
#     user_journey, pos, edge_color='black', width=1, linewidths=1,
#     node_size=500, node_color='pink', alpha=0.9,
#     labels={node: node for node in user_journey.nodes()}
# )
# nx.draw_networkx_edge_labels(
#     user_journey, pos,
#     edge_labels={('A', 'B'): 'AB', 
#                  ('B', 'C'): 'BC', 
#                  ('B', 'D'): 'BD'},
#     font_color='red'
# )
# plt.axis('off')
# plt.show()

fig, ax = plt.subplots()
# plt.show()

for step in USER_1_1:
    print(step)
    # user_journey.add_edge(step[0], step[1])
    user_journey.add_edges_from([step])
    pos = nx.spring_layout(user_journey)
    print("hello")
    # plt.clf()
    plt.close()
    nx.draw(
        user_journey, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', 
        labels={node: node for node in user_journey.nodes()}
    )
    plt.show()
    


# with plt.xkcd():
#     fig, ax = plt.subplots(figsize=(5, 5))
#     x = ig.plot(
#             g,
#             target=ax,
#             layout='kk',
#             vertex_size=0.3,
#             edge_width=4,
#             vertex_label=range(g.vcount()),
#             vertex_color="white",
#         )
#     plt.draw()

"""
TODO:

1. User follows these edges in order:
[
    ["LOGIN", "ACCOUNT A"],
    ["ACCOUNT A", "ACCOUNT B"],
    ["ACCOUNT B", "ACCOUNT CUSTOMER FACING"],
]
nothing wrong

2. User follows these edges in order:
[
    ["LOGIN", "ACCOUNT A"],
    ["ACCOUNT A", "ACCOUNT B"],
    ["ACCOUNT B", "ACCOUNT CUSTOMER FACING"],
    ["ACCOUNT A", "ACCOUNT DATA FACING"], # BLOCKED, conflict of interest between ACCOUNT CUSTOMER FACING and ACCOUNT DATA FACING
]

3. User follows these edges in order:
[
    ["ACCOUNT A", "ACCOUNT B"], # BLOCKED, not through verified entry
]


BLOCKED could also be just an alert
"""