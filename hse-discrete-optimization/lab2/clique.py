import cplex
import sys
import networkx as nx
import time
import multiprocessing
from utils import parser

max_clique = []

def independent_sets(G):
    # color graph in different ways to get sets ASAP
    all_strategies = [
        nx.coloring.strategy_connected_sequential_bfs,
        nx.coloring.strategy_connected_sequential_dfs,
        nx.coloring.strategy_independent_set,
        nx.coloring.strategy_largest_first,
        nx.coloring.strategy_random_sequential,
        nx.coloring.strategy_saturation_largest_first,
        nx.coloring.strategy_smallest_last
    ]
    independent_sets = []
    for strategy in all_strategies:
        GC = nx.coloring.greedy_color(G, strategy=strategy)
        for color in set(color for node, color in GC.items()):
            independent_sets.append(
                [node1 for node1, color1 in GC.items() if color1 == color])

    if len(G.nodes()) < 200:   # slow on large graphs
        for independent_set in independent_sets:
                # consider candidates only for one vertex undependent set
                # because if it's not candidate for all then it will not be included
            candidates = list(nx.complement(G)[independent_set[0]].keys())
            for candidate in candidates:
                if candidate not in independent_set:
                    canBeAdded = True
                    for node in independent_set:
                        if node!=candidate:
                            if G.has_edge(node, candidate):
                                canBeAdded = False
                                break
                    if (canBeAdded):
                        independent_set.append(candidate)
    return independent_sets

def base_model_solution(independent_sets, vertex_number, G):
    problem = cplex.Cplex()    
    problem.set_log_stream(None)
    problem.set_error_stream(None)
    problem.set_warning_stream(None)
    problem.set_results_stream(None)
    problem.objective.set_sense(problem.objective.sense.maximize)
    types = 'C' * vertex_number    
    problem.variables.add(obj=[1.0] * vertex_number,
                          ub=[1.0] * vertex_number,
                          names=['x{0}'.format(x) for x in range(1,vertex_number+1)], types = types)
    constraints = []
    not_connected = nx.complement(G).edges()
    for ind_set in independent_sets: 
        constraints.append([['x{0}'.format(i) for i in ind_set], [1.0] * len(ind_set)])
    for i, j in not_connected: 
        constraints.append([['x{0}'.format(i), 'x{0}'.format(j)], [1.0] * 2])

    problem.linear_constraints.add(lin_expr = constraints,
                                   senses = [ 'L' ] * (len(independent_sets) + len(not_connected)),
                                   rhs = [1.0] * (len(independent_sets) + len(not_connected)),
                                   names = ['c{0}'.format(x) for x in range(len(independent_sets)+len(not_connected))])
    return problem

            
def get_non_zero_variables(solution):
    return {i: value for i, value in enumerate(solution) if abs(value) > sys.float_info.epsilon} 

def get_branch_var(non_zero_variables): # вернёт номер вершины для ветвления 
    not_integer_vars_dict = {vertex: value for vertex, value in non_zero_variables.items() 
                                    if abs(value - 1) > sys.float_info.epsilon} 
    if len(not_integer_vars_dict) == 0:
        return None
    return max(not_integer_vars_dict, key=not_integer_vars_dict.get)



def branching(problem):
    global max_clique
    def branching_constraint(problem, branching_var, set_to_one):
        if (set_to_one):
            problem.variables.set_lower_bounds(branching_var,1.0)
            problem.variables.set_upper_bounds(branching_var,1.0)
        else:
            problem.variables.set_upper_bounds(branching_var,0.0)
        return problem

    problem.solve()
    solution = problem.solution.get_values()
    non_zero = get_non_zero_variables(solution)
    if sum(solution)>len(max_clique):
        var = get_branch_var(non_zero)
        if var != None:
            branching(branching_constraint(problem, var, False))
            branching(branching_constraint(problem, var, True))              
            problem.variables.set_lower_bounds(var,0.0)
            problem.variables.set_upper_bounds(var,1.0)

        else:
            max_clique = list(x+1 for x in non_zero.keys())
            return 0 
    return max_clique

def validate_clique(clique, graph):
    for x in clique:
        for y in clique:
            if x!=y:
                if not graph.has_edge(x, y):
                    print ("Sorry. Wrong answer :(")

def find_clique(filename):
    time_start = time.time()
    G = parser(filename)
    global max_clique
    max_clique = []
    problem = base_model_solution(independent_sets(G),G.number_of_nodes(),G)
    branching(problem)
    time_finish = time.time()
    print("Max clique:", len(max_clique))
    validate_clique(max_clique, G)
    print("Time:", int(round(time_finish - time_start, 4) * 1000), 'ms')

    return max_clique

def find_clique_multi(filename):
    proc = multiprocessing.Process(target=find_clique, args=[filename])
    proc.start()
    proc.join()
