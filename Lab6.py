from queue import PriorityQueue


# import networkx as nx

class Graph:

    def __init__(self, graph_dict=dict()) -> None:
        self._graph_dict = graph_dict

    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = set()

    def remove_edge(self, edge: tuple):
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

    def remove_vertex(self, vertex: str):
        self._graph_dict.pop(vertex, None)

        for key, val in self._graph_dict.items():
            for connection in val:
                _vertex, _weight = connection

                if vertex == _vertex:
                    self._graph_dict[key].remove(connection)
                    break

    def neighbors(self, vertex):
        return self._graph_dict[vertex]


def dijkstra(current_graph: Graph, start_position: str, final_position: str):
    variants = PriorityQueue()
    variants.put(start_position, 0)
    came_from = {}
    current_cost = {}
    came_from[start_position] = None
    current_cost[start_position] = 0
    current = None

    while not variants.empty():
        current = variants.get()
        #print(current)

        # if current[0] == final_position:
        #     return get_final_path(came_from, start_position, final_position)

        for next in current_graph.neighbors(current[0]):
            new_cost = current_cost[current[0]] + next[1]
            if next[0] not in current_cost or new_cost < current_cost[next[0]]:
                current_cost[next[0]] = new_cost

                priority = new_cost
                variants.put(next[0], priority)
                came_from[next[0]] = current[0]

    # current = variants.get()

    if final_position in came_from.keys():
        #print(came_from)
        return get_final_path(came_from, start_position, final_position), current_cost[final_position]

    return None


def get_final_path(paths: list(), start, final):
    current = final
    result = list()
    while True:
        result.append(current)
        #print(current)
        if current == start:
            return result[::-1]

        current = paths[current]


graph = Graph()

graph.add_vertex("a")  # 0
graph.add_vertex("b")  # 1
graph.add_vertex("c")  # 2
graph.add_vertex("d")  # 3
graph.add_vertex("e")  # 4
graph.add_vertex("f")  # 5
graph.add_vertex("g")  # 6
graph.add_vertex("h")  # 7
graph.add_vertex("j")  # 8

graph.add_edge(("a", "b", 2))
graph.add_edge(("a", "c", 6))
graph.add_edge(("a", "d", 8))
graph.add_edge(("a", "g", 3))

graph.add_edge(("b", "c", 9))
graph.add_edge(("b", "d", 3))
graph.add_edge(("b", "f", 4))
graph.add_edge(("b", "g", 9))

graph.add_edge(("c", "d", 7))

graph.add_edge(("d", "e", 5))
graph.add_edge(("d", "f", 5))

graph.add_edge(("e", "g", 8))
graph.add_edge(("e", "h", 9))

graph.add_edge(("f", "h", 6))
graph.add_edge(("f", "j", 4))
graph.add_edge(("j", "h", 1))

# print(dijkstra(graph, "a", "h"))
roots = {}
lenghts = {}
roots[len(roots)], lenghts[len(lenghts)] = dijkstra(graph, 'a', 'h')
# print(dijkstra(graph, roots[0][0], roots[0][1]))

def show_roots(roots, lengths):
    print(f"Roots \t\t Lengths")
    for root in roots:
        print(f'{roots[root]} \t\t {lenghts[root]}')


show_roots(roots, lenghts)
# print(roots[0])

def yen_algos(roots:list, step:int, graph: Graph, start, finish):
    CopyOfGraph = Graph()
    CopyOfGraph = graph
    arrayOfLenght = []
    arrayOfLetters = []
    candi, lenOfCandi = [], []
    prev_vertex = None
    str = []
    for i in range(step+1):
        current_vertex = roots[0][i]
        if current_vertex == finish:
            print(f'{i-1} steps is good for that graphs')
            break
        next_vertex = roots[0][i+1]
        a, b = dijkstra(CopyOfGraph, current_vertex, next_vertex)
        arrayOfLenght.append(b)
        if len(arrayOfLenght)>1:
            arrayOfLenght[-1] += arrayOfLenght[-2]
        arrayOfLetters.append(a)
        if i == 0:
            CopyOfGraph.remove_edge((current_vertex, next_vertex))
            a, b = dijkstra(CopyOfGraph, current_vertex, finish)
            candi.append(a)
            lenOfCandi.append(b)
            print()
            print(arrayOfLenght)
            print()
            prev_vertex = current_vertex
            # CopyOfGraph.remove_vertex()
        elif step == len(roots[0]):
            print("hehe, boi")
            break
        else:
            CopyOfGraph.remove_vertex(prev_vertex)
            CopyOfGraph.remove_edge((current_vertex, next_vertex))
            a, b, = dijkstra(CopyOfGraph, current_vertex, finish)
            b = b + arrayOfLenght[-1]
            print('b')
            print(b)
            print('array')
            print(arrayOfLenght)
            print()
            a.insert(0, str)
            str.append(prev_vertex)
            candi.append(a)
            lenOfCandi.append(b)
            prev_vertex = current_vertex
    return candi, lenOfCandi

canditates = []
lenOfCandi = []
canditates, lenOfCandi = yen_algos(roots, 2 , graph, 'a', 'h')
print(canditates)
print(lenOfCandi)


# print(dijkstra(graph, roots[0][0], roots[0][1]))
# print(canditates, candi_len)
