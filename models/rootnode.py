from models.controlnode import ControlNode


class RootNode:
    nodes = None

    def __init__(self, node_count, marker_count):
        self.nodes = []
        for x in range(node_count):
            self.nodes.append(ControlNode(marker_count))

    def randomize(self):
        for n in self.nodes:
            n.randomize()