import time
import random

from multiprocessing import current_process
from distsim import Network, Node, Link, Message


def node_code(number_of_nodes):
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    # fill code here


def client_code(number_of_nodes):
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    possible_nodes = [str(idx) for idx in range(number_of_nodes)]

    while True:
        target = random.choice(possible_nodes)
        source = random.choice(possible_nodes)

        msg = Message(node.name, target)
        logger.info(f"Sending {msg} to {source}")
        node.send_to(source, msg)

        time.sleep(2)


if __name__ == "__main__":
    number_of_nodes = 8

    nodes = [Node(str(idx), node_code, (number_of_nodes,)) for idx in range(number_of_nodes)]
    # each node will have link to each other node
    links = [Link(str(i), str(j)) for j in range(number_of_nodes) for i in range(number_of_nodes) if i != j]

    client_node = [Node("client", client_code, (number_of_nodes,))]
    client_links = [Link("client", str(i)) for i in range(number_of_nodes)]

    network = Network(nodes + client_node, links + client_links)

    network.start()
    time.sleep(5)
    network.kill()
