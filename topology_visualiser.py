import networkx as nx
import matplotlib.pyplot as plt


def create_topology(mininet_net):
    # Create an empty directed graph using NetworkX
    topology = nx.DiGraph()

    # Iterate over the hosts in the Mininet network and add them to the topology graph
    for host in mininet_net.hosts:
        topology.add_node(host.name, type='host', ip=host.IP())

    # Iterate over the switches in the Mininet network and add them to the topology graph
    for switch in mininet_net.switches:
        topology.add_node(switch.name, type='switch')

    # Iterate over the links in the Mininet network and add them to the topology graph
    for link in mininet_net.links:
        src_node = link.intf1.node
        dst_node = link.intf2.node
        src_port = link.intf1.name.split('-')[-1]
        dst_port = link.intf2.name.split('-')[-1]
        topology.add_edge(src_node, dst_node, src_port=src_port, dst_port=dst_port)

    return topology


def display_topology(topology):
    # Draw the topology graph using NetworkX and Matplotlib
    pos = nx.spring_layout(topology)
    host_nodes = [node for node, attr in topology.nodes(data=True) if attr['type'] == 'host']
    switch_nodes = [node for node, attr in topology.nodes(data=True) if attr['type'] == 'switch']
    nx.draw_networkx_nodes(topology, pos, nodelist=host_nodes, node_color='r', node_size=500, alpha=0.8)
    nx.draw_networkx_nodes(topology, pos, nodelist=switch_nodes, node_color='b', node_size=500, alpha=0.8)
    nx.draw_networkx_edges(topology, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(topology, pos, font_size=10, font_color='w')
    plt.axis('off')
    plt.show()


