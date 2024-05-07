import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._nodi = DAO.get_all_airports()
        self._grafo = nx.Graph()
        self._idMap = {}
        for f in self._nodi:
            self._idMap[f.ID] = f
        self._lista_collegamenti = set()


    def buildGraph(self, distance):
        self._grafo.add_nodes_from(self._nodi)
        edges = DAO.get_all_voli(distance)
        for c in edges:
            u_nodo = self._idMap[c.ORIGIN_AIRPORT_ID]
            v_nodo = self._idMap[c.DESTINATION_AIRPORT_ID]
            if self._grafo.has_edge(u_nodo, v_nodo) is False:
                self._grafo.add_edge(u_nodo, v_nodo, weight=c.DISTANCE)
                self._lista_collegamenti.add(f"Added edge between {u_nodo} and {v_nodo}")
        return self._lista_collegamenti


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
