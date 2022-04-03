
# Module: tree_search
# 
# This module provides a set o classes for automated
# problem solving through tree search:
#    SearchDomain  - problem domains
#    SearchProblem - concrete problems to be solved
#    SearchNode    - search tree nodes
#    SearchTree    - search tree with the necessary methods for searhing
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2019,
#  Inteligência Artificial, 2014-2019

from abc import ABC, abstractmethod

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self, state, goal):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):  # recebe dominio, origem e destino
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state): # testa se chegámos ao objetivo
        return self.domain.satisfies(state,self.goal)

# Nós de uma arvore de pesquisa
class SearchNode:   # representa todos os nós
    def __init__(self, state, parent, depth=0, cost=0, heuristic=0):    # estado atual e nó pa
        self.state = state  
        self.parent = parent
        self.depth = depth  # added for ex2 (!) registers node's depth - começa em 0
        self.cost = cost    # added for ex7 (!)

        self.heuristic = heuristic # added for ex11/12 (!)
    
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    
    def __repr__(self):
        return str(self)

     # evitar loop infinito (ex1)
    def in_parent(self, state):
        if self.parent == None:
            return False
        return self.state == state or self.parent.in_parent(state)


# Arvores de pesquisa
class SearchTree:       # core da aula (!)

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem # problema a resolver (uma instância de SearchProblem)
        root = SearchNode(problem.initial, None, 0, 0, 0)
        self.open_nodes = [root]    # nó inicial (que é a cidade de onde queremos sair)
        self.strategy = strategy
        self.solution = None
        self.length = 0         # added for ex3 (!) returns length of the solution found
        self.terminals = 1      # added for ex5 (!)
        self.non_terminals = 0  # added for ex5 (!)
        self.avg_branching = 0  # added for ex6 (!)
        self.highest_cost_nodes = [root] # added for ex15 (!)

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)


    #procurar a solucao
    def search(self, limit=None):
        while self.open_nodes != []:    # se tiver vazio já n ha caminhos p verificar
            node = self.open_nodes.pop(0)   # tira 1º nó e começa a analiza-lo
           
            if self.problem.goal_test(node.state):  # testar se é o objetivo (cidade destino)    
                self.solution = node
                self.length = self.solution.depth # added for ex3 (!) update the length (Which was 0 to the node depth returned)
                self.terminals = len(self.open_nodes)          # solution node is terminal, so we add +1
                self.avg_branching = round(((self.terminals + self.non_terminals - 1) / self.non_terminals), 2)  # media
                self.cost = self.solution.cost
                
                return self.get_path(node)

            lnewnodes = []
            self.non_terminals += 1   # added for ex5 (!) to register number of non terminal nodes

            for a in self.problem.domain.actions(node.state):   # procura agora todas as opçoes possiveis da cidade atual onde estamos até ao destino que queremos
                newstate = self.problem.domain.result(node.state, a)
                # node.depth +1 for ex3 (!)
                # node.cost + self.problem.domain.cost(node.state, a) for ex8 (!)
                # self.problem.domain.heuristic(newstate,self.problem.goal) for ex11/12 (!)
                newnode = SearchNode(newstate, node, node.depth + 1, 
                                                     node.cost + self.problem.domain.cost(node.state, a),
                                                     self.problem.domain.heuristic(newstate,self.problem.goal)
                                    )


                if not node.in_parent(newstate) and (limit == None or newnode.depth <= limit):    # ex1 prevent cycles (!) and ex4 (!) to support depth search with limit
                    lnewnodes.append(newnode)     

                     
                # added for ex15 (!)
                if node.cost > self.highest_cost_nodes[0].cost:
                    self.highest_cost_nodes = [node]
                elif node.cost == self.highest_cost_nodes[0].cost and node not in self.highest_cost_nodes:
                    self.highest_cost_nodes.append(node)

            self.add_to_open(lnewnodes)

        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)   
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':   # added for ex10 (!)
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key=lambda node : node.cost)
        elif self.strategy == 'greedy': # added for ex13 (!)
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key=lambda node : node.heuristic)
        elif self.strategy == 'a*':     # added for ex14(!) TA MAL
            self.open_nodes= sorted(self.open_nodes + lnewnodes, key=lambda node: node.cost + node.heuristic)
            #self.open_nodes = sorted(key =lambda node: node.cost + node.heuristic)

    
    # def get_length(self):   # ex3 (!)
    #     if self.length != None:
    #         return self.length 
    
    # def get_t(self):    # ex5 (!)
    #     return self.terminals, self.non_terminals
    
    # def get_avg(self):  # ex6 (!)
    #     return self.avg_branching
