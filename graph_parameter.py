from gurobipy import tuplelist
import pandas as pd
import numpy as np

def graph_parameter(node_file="Nodes_Revised.csv", arc_file="Arcs.csv", commodities_file="Commodities.csv"):
    # data setup into pandas df's
    node_df = pd.read_csv(node_file)
    arc_df = pd.read_csv(arc_file)
    commodities_df = pd.read_csv(commodities_file)

    # comodities and quantity {commodity:quantity}
    commodity_quantity = {k: g['weight'].values[0] for k, g in commodities_df.groupby('name')}

    # nodes
    nodes = node_df['nodes'].tolist()

    # arcs (tuplelist)
    arcs = tuplelist([tuple(pair) for pair in arc_df.values])

    # sources {commodity:source}
    commodity_source = {k: g['source'].values[0] for k, g in commodities_df.groupby('name')}

    # sinks {commodity:sink}
    commodity_sink = {k: g['sink'].values[0] for k, g in commodities_df.groupby('name')}
    
    # m_distance {(arc pair): euclidean distance}
    m_distance = {(x, y):np.sqrt(x**2 + y**2) for x, y in arcs}

    return commodity_quantity, nodes, arcs, commodity_source, commodity_sink, m_distance

if __name__ == "__main__":
    print(graph_parameter())