def transit_node_routing(nodes, important_nodes, distances):
    transit_nodes = []

    for node in nodes:
        if node in important_nodes:
            transit_nodes.append(node)

    routes = {}

    for node1 in transit_nodes:
        for node2 in transit_nodes:
            if node1 != node2:
                distance = distances.get((node1, node2))
                if distance:
                    if node1 not in routes:
                        routes[node1] = {}
                    routes[node1][node2] = distance

    return routes

nodes = ["A", "B", "C", "D", "E"]
important_nodes = ["A", "C", "E"]
distances = {
    ("A", "B"): 5,
    ("A", "C"): 10,
    ("B", "C"): 3,
    ("B", "D"): 8,
    ("C", "D"): 2,
    ("C", "E"): 6,
    ("D", "E"): 7
}

result = transit_node_routing(nodes, important_nodes, distances)
print(result)
