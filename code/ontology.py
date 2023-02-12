from onto_master.onto import Onto
import networkx as nx
import datetime as dt
import time

class Ontology(object):
    def __init__(self, filepath:str) -> None:
        self.filepath = filepath
        self.filename = filepath.split('/')[-1]

        ontology = Onto.load_from_file(filepath)
        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.__create_node_list(ontology))
        self.graph.add_edges_from(self.__create_edge_list(ontology))

    def __create_node_list(self, ontology: Onto) -> list[tuple[int, dict]]:
        result = []
        for node in ontology.nodes():
            id = node['id']
            attr = dict()
            for key, value in node.items():
                attr[key]=value
            result.append((id, attr))
        return result
    
    def __create_edge_list(self, ontology: Onto) -> list[tuple[int,int,dict]]:
        result = []
        for edge in ontology.links():
            edge_from = edge['source_node_id']
            edge_to = edge['destination_node_id']
            attr = dict()
            for key, value in edge.items():
                attr[key] = value
            result.append((edge_from, edge_to, attr))
        return result

    def get_nodes_names(self):
        for node in list(self.graph.nodes):
                yield (node, self.graph.nodes[node]['name'])


    def __get_nodes_from_one_to_others(self, from_node, to_nodes:list) -> set[str]:
        '''
        Finds all the vertices that need to be visited from one vertex to another.
        @param from_node - ID of key node.
        @param to_nodes - IDs of another nodes.
        @return set of nodes between key node and another nodes.
        '''
        nodes_set = set()
        for to_node in to_nodes:
            path_nodes = nx.bidirectional_shortest_path(self.graph, from_node, to_node)
            nodes_set.update(set(path_nodes))
        return nodes_set

    def __get_all_nodes_in_subgraph(self, node_ids: list[str]):
        '''
        Finds all intermediate nodes.
        @param node_ids - IDs of nodes.
        @return set of all intermediate nodes.
        '''
        nodes_set = set()
        for i in range(len(node_ids) - 1):
            key_id  = node_ids[i]
            others_ids = node_ids[i+1:]
            nodes_set.update(self.__get_nodes_from_one_to_others(key_id, others_ids))
        return nodes_set

    def __get_ontology(self, graph) -> Onto:
        onto = Onto.empty()
        nodes_store = dict()
        for id, attr in graph.nodes.items():
            nodes_store[id] = onto.add_node(attr['name'], attr['position_x'], attr['position_y'], attr['attributes'])
        for _, attr in graph.edges.items():
            src, dst = attr['source_node_id'], attr['destination_node_id']
            onto.link_nodes(nodes_store[src], nodes_store[dst], attr['name'], attr['attributes'])
        return onto


    def write_connected_subgraph(self, node_ids: list[str], filename:str):
        nodes = self.__get_all_nodes_in_subgraph(node_ids)
        subgraph = self.graph.subgraph(nodes)
        onto = self.__get_ontology(subgraph)
        date = dt.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d %H_%M_%S')
        onto.write_to_file(date + ' ' + filename)


    def get_num_of_different_paths(self, from_node, to_node, max_length:int) -> int:
        return len(list(nx.all_simple_paths(self.graph, from_node, to_node, max_length)))



if __name__ == '__main__':
    onto = Ontology('./documents/IZ_Kolesnikov_A_S__PMI-2-22.ont')
    print(list(onto.graph.nodes))
    # print(onto.graph.nodes[list(onto.graph.nodes.keys())[0]])
    # for name in onto.get_nodes_names():
    #     print(name)

    # print(nx.bidirectional_shortest_path(onto.graph, '1', '6'))
    # onto.build_connected_subgraph(['1', '3','4','101'])

    # [print(id, attr['name'], attr['position_x'], attr['position_y'], attr['attributes']) for id, attr in onto.graph.nodes.items()]
    # [print(id, attr['source_node_id'], attr['destination_node_id'], attr['name'], attr['attributes']) for id, attr in onto.graph.edges.items()]

