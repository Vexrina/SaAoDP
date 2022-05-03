import itertools
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
import math
from queue import PriorityQueue

class Graph:

    def __init__(self, graph_dict=dict()) -> None:
        self._graph_dict = graph_dict
        self.Visual = nx.Graph()
        self.mtx = None

    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = set()
            self.Visual.add_node(vertex)

    def remove_edge(self, edge: tuple):#только для Йена
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                for connection in self._graph_dict[x]:
                    _vertex, _weight = connection
                    if _vertex == y:
                        self._graph_dict[x].remove(connection)
                        break

    def add_edge(self, edge: tuple()):
        vertex1, vertex2, weight = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add((y, weight))
            else:
                self._graph_dict[x] = {(y, weight)}
        self.Visual.add_edge(vertex1, vertex2)
        self.Visual[vertex1][vertex2]['weight']=weight

    def remove_vertex(self, vertex: str):#Только для Йена
        self._graph_dict.pop(vertex, None)

        for key, val in self._graph_dict.items():
            for connection in val:
                _vertex, _weight = connection

                if vertex == _vertex:
                    self._graph_dict[key].remove(connection)
                    break

    def neighbors(self, vertex):
        return self._graph_dict[vertex]
    
    def Visualize(self):
        nx.draw_circular(self.Visual,
         node_color='red',
         node_size=1000,
         with_labels=True)
    
    def SaveMTX(self, mtx):
        self.mtx = mtx

    def ShowMTX(self):
        for i in range(len(self.mtx)):
            print(self.mtx[i])
    
    def GetMTX(self):
        return self.mtx
    
    def GetNumberOfVertex(self):
        return len(self.mtx)


graph = Graph()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def MtxToGraph(mtx, graph:Graph):
    for i in range (len(mtx)):
        graph.add_vertex(alphabet[i])
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            if i == j:
                continue
            elif mtx[i][j] == math.inf:
                continue
            else:
                graph.add_edge((alphabet[i],alphabet[j], mtx[i][j]))

    graph.SaveMTX(mtx)
Q = math.inf
            #a  b  c  d  e  f  g  h  i (1,2,3,4,5,6,7,8,9)
testMTX = [ [0, 2, 6, 8, Q, Q, 3, Q, Q],#a
            [2, 0, 9, 3, Q, 4, 9, Q, Q],#b
            [6, 9, 0, 7, Q, Q, Q, Q, Q],#c
            [8, 3, 7, 0, 5, 5, Q, Q, Q],#d
            [Q, Q, Q, 5, 0, Q, 8, 9, Q],#e
            [Q, 4, Q, 5, Q, 0, Q, 6, 4],#f
            [3, 9, Q, Q, 8, Q, 0, Q, Q],#g
            [Q, Q, Q, Q, 9, 6, Q, 0, 1],#h
            [Q, Q, Q, Q, Q, 4, Q, 1, 0],#i                                                  
                                        ]
MtxToGraph(testMTX, graph)



def get_Floyd_path( vertexNumberList, start, end):
    global alphabet
    path = [alphabet[end]]
    while end != start:
        letter = alphabet[vertexNumberList[end][start]]
        end = vertexNumberList[end][start]
        path.insert(0,letter)
    return path

def Floyd(graph:graph, start, end):
    global alphabet
    numberOfVertex = graph.GetNumberOfVertex()
    MtxOfGraph = graph.GetMTX().copy()
    vertexNumberList = [[v for v in range(numberOfVertex)] for u in range(numberOfVertex)]
    for k in range(numberOfVertex):
        for i in range(numberOfVertex):
            for j in range(numberOfVertex):
                temp = MtxOfGraph[i][k] + MtxOfGraph[k][j]
                if MtxOfGraph[i][j]>temp:
                    MtxOfGraph[i][j] = temp
                    vertexNumberList[i][j] = k
    print(get_Floyd_path( vertexNumberList, start, end))

Floyd(graph, 0, 7)