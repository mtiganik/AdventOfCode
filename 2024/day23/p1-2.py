import networkx as nx
G = nx.Graph(line.strip().split("-") for line in open("input.txt"))

# noe = G.nodes()

cliques = list(nx.enumerate_all_cliques(G))
print(sum(any(a[0] == 't' for a in c) for c in cliques if len(c) == 3))

