import copy

import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._nodi = DAO.get_all_airports()
        self._grafo = nx.Graph()
        self._mappa = {}
        for f in self._nodi:
            self._mappa[f.ID] = f

    def buildGraph(self, distanza):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._nodi)
        self.addEdgesPesati()
        return self.getArchiPesoMaggiore(int(distanza))

    def addEdgesPesati(self):
        "utilizzo questa funzione per assegnare al grafo un peso = distanza media"
        self._grafo.clear_edges()
        connessione = DAO.get_media_tratta()
        for c in connessione:
            if self._grafo.has_edge(self._mappa[c.ORIGIN_AIRPORT_ID],
                                    self._mappa[c.DESTINATION_AIRPORT_ID]):
                self._grafo[self._mappa[c.ORIGIN_AIRPORT_ID]][self._mappa[c.DESTINATION_AIRPORT_ID]]['weight'] += [c.DISTANCE*c.CONTATORE, c.CONTATORE]
            else:
                self._grafo.add_edge(self._mappa[c.ORIGIN_AIRPORT_ID], self._mappa[c.DESTINATION_AIRPORT_ID], weight=[c.DISTANCE*c.CONTATORE, c.CONTATORE])

    def getArchiPesoMaggiore(self, distanza):
        """Print di archi con peso maggiore di 1 (agisce solo sul grafo pesato)
        """
        if len(self._grafo.edges) == 0:
            print("Il grafo è vuoto")
            return

        edges = self._grafo.edges
        result = []

        for u, v in edges:
            peso = round(self._grafo[u][v]["weight"][0]/self._grafo[u][v]["weight"][1], 1)
            if peso > distanza:
                result.append((u, v, peso))
            else:
                self._grafo.remove_edge(u, v)
        return result

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getPesoGrafo(self, u, v):
        return self._grafo[u][v]['weight']
