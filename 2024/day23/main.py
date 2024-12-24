import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(line.strip().split("-") for line in open("input.txt"))

cliques = list(nx.enumerate_all_cliques(G))

print("p1:",sum(any(k[0] == "t" for k in cliq) for cliq in cliques if len(cliq) == 3))
print("p2:", ",".join(sorted(max(cliques, key=len))))

