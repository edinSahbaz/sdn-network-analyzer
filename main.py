from mininet.net import Mininet
from mininet.topo import Topo
from topology_visualiser import create_topology, display_topology
import controller
import packet_analyzer


def visualiser():
    # Create a Mininet network
    net = Mininet(topo=Topo())

    # Start the network
    net.start()

    # Create the network topology
    topology = create_topology(net)

    # Display the network topology
    display_topology(topology)

    # Stop the network
    net.stop()


def main():
    controller.RyuController()
    visualiser()
    packet_analyzer.main()


if __name__ == '__main__':
    main()