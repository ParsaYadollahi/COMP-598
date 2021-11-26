import argparse
from io import TextIOWrapper
import json
import networkx as nx
from networkx.algorithms.centrality.betweenness import betweenness_centrality
from networkx.classes.graph import Graph


'''
  python compute_network_stats.py -i /path/to/<interaction_network.json> -o /path/to/<stats.json>
'''
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


  f = open(out_file, "w")

  # Q1 - most_connected_by_num
  top_connected_edges = {}
  for node in G.nodes():
    top_connected_edges[node] = G.degree(node)
  top_connected_edges = sorted(top_connected_edges, key=top_connected_edges.get, reverse=True)[:3]
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

  f.write("\t\"most_connected_by_weight\": [")
  for x in top_connected_by_weight:
    f.write('"%s"' %x)
    if (x == top_connected_by_weight[-1]):
      break
    f.write(', ')
  f.write('],\n')


  # Q3 - most_central_by_betweenness
  b_c_list = list(betweenness_centrality(G).items())
  b_c_list.sort(key=lambda x:x[1], reverse=True)
  i = 0
  f.write("\t\"most_central_by_betweenness\": [")
  for v in b_c_list[:3]:
    f.write('"%s"' %v[0])
    if i == 2:
      break
    i += 1
    f.write(', ')
  f.write(']\n')
  f.write('}')

  f.close()

if __name__ == '__main__':
  main()
