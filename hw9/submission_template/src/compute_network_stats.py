import argparse
from io import TextIOWrapper
import json
import networkx as nx
from networkx.algorithms.centrality.betweenness import betweenness_centrality
from networkx.classes.graph import Graph

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', help='The input file of this script.', required=True)
  parser.add_argument('-o', help='The output file of this script.', required=False)

  args = parser.parse_args()
  in_file = args.i
  out_file = args.o

  f: TextIOWrapper = open(in_file, 'r')
  data: dict = json.load(f)
  G: Graph = nx.Graph()

  for character, interactions in data.items():
    for inter_char, num_inter in interactions.items():
      G.add_edge(character, inter_char, weight=num_inter)
  print(G)


  f = open(out_file, "w")

  # Q1 - most_connected_by_num
  top_connected_edges = {}
  for node in G.nodes():
    top_connected_edges[node] = G.degree(node)
  top_connected_edges = sorted(top_connected_edges, key=top_connected_edges.get, reverse=True)[:3]
  print(top_connected_edges)
  f.write('{\n')

  f.write("\t\"most_connected_by_num\": [")
  for x in top_connected_edges:
    f.write('"%s"' %x)
    if (x == top_connected_edges[-1]):
      break
    f.write(', ')

  f.write('],\n')


  # Q2 - most_connected_by_weight
  top_connected_by_weight = {node_name: 0 for node_name in G.nodes()}
  for node in G.nodes():
    for _, weight in G[node].items():
      top_connected_by_weight[node] += weight['weight']
  top_connected_by_weight = sorted(top_connected_by_weight, key=top_connected_by_weight.get, reverse=True)[:3]
  print(top_connected_by_weight)

  f.write("\t\"most_connected_by_weight\": [")
  for x in top_connected_by_weight:
    f.write('"%s"' %x)
    if (x == top_connected_by_weight[-1]):
      break
    f.write(', ')

  f.write('],\n')

  f.write('\n}')


  print(betweenness_centrality(G))


if __name__ == '__main__':
  main()
