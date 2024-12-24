import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(line.strip().split("-") for line in open("input.txt"))

cliques = list(nx.find_cliques(G))



largest = max(cliques, key=len)
print("!!")
sorted = sorted(largest)
sorted = str(sorted).replace(" ","").replace("[","").replace("]","").replace("'","")
print(str(sorted))

