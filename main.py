import osmnx as ox

# Configure the place, network type, and specify that you want to retain all
place = 'Atlanta, Georgia, USA'
network_type = 'drive'
ox.config(use_cache=True, log_console=True)

# Fetch OSM street network from the specified place
graph = ox.graph_from_place(place, network_type=network_type)

# Plot the street network and save to disk
fig, ax = ox.plot_graph(ox.project_graph(graph), show=False, close=True)
fig.savefig('atlanta_streets.png')