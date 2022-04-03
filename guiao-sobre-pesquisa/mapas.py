from constraintsearch import *

region = ['A', 'B', 'C', 'D', 'E']
colors = ['red', 'blue', 'green', 'yellow', 'white']

def color_constraint(r1,c1,r2,c2):
    return c1!=c2

# n = alinea do esquema (ver guião prático IV.4)
def make_constraint_graph(n):
    
    if n == 'a':
        graph =  { ('A', 'B'): color_constraint}
        graph.update({ ('A', 'D'): color_constraint})
        graph.update({ ('A', 'E'): color_constraint})
        
        graph.update({ ('D', 'A'): color_constraint})
        graph.update({ ('D', 'E'): color_constraint})
        graph.update({ ('D', 'C'): color_constraint})
        
        graph.update({ ('C', 'B'): color_constraint})
        graph.update({ ('C', 'E'): color_constraint})
        graph.update({ ('C', 'D'): color_constraint})
        
        graph.update({ ('B', 'A'): color_constraint})
        graph.update({ ('B', 'E'): color_constraint})
        graph.update({ ('B', 'C'): color_constraint})
        
        graph.update({ ('E', 'A'): color_constraint})
        graph.update({ ('E', 'B'): color_constraint})
        graph.update({ ('E', 'C'): color_constraint})
        graph.update({ ('E', 'D'): color_constraint})
        return graph
    
    elif n == 'b':
        graph =  { ('A', 'B'): color_constraint}
        graph.update({ ('A', 'D'): color_constraint})
        graph.update({ ('A', 'E'): color_constraint})
        
        graph.update({ ('D', 'A'): color_constraint})
        graph.update({ ('D', 'E'): color_constraint})
        graph.update({ ('D', 'F'): color_constraint})
        
        graph.update({ ('C', 'B'): color_constraint})
        graph.update({ ('C', 'E'): color_constraint})
        graph.update({ ('C', 'F'): color_constraint})
        
        graph.update({ ('B', 'A'): color_constraint})
        graph.update({ ('B', 'E'): color_constraint})
        graph.update({ ('B', 'C'): color_constraint})
        
        graph.update({ ('E', 'A'): color_constraint})
        graph.update({ ('E', 'B'): color_constraint})
        graph.update({ ('E', 'C'): color_constraint})
        graph.update({ ('E', 'D'): color_constraint})
        graph.update({ ('E', 'F'): color_constraint})
        
        graph.update({ ('F', 'D'): color_constraint})
        graph.update({ ('F', 'E'): color_constraint})
        graph.update({ ('F', 'C'): color_constraint})
        return graph
    
    elif n == 'c':
        graph =  { ('A', 'B'): color_constraint}
        graph.update({ ('A', 'F'): color_constraint})
        graph.update({ ('A', 'E'): color_constraint})
        graph.update({ ('A', 'D'): color_constraint})
        
        graph.update({ ('B', 'F'): color_constraint})
        graph.update({ ('B', 'A'): color_constraint})
        graph.update({ ('B', 'C'): color_constraint})
        
        graph.update({ ('C', 'B'): color_constraint})
        graph.update({ ('C', 'F'): color_constraint})
        graph.update({ ('C', 'G'): color_constraint})
        graph.update({ ('C', 'D'): color_constraint})
        
        graph.update({ ('D', 'A'): color_constraint})
        graph.update({ ('D', 'E'): color_constraint})
        graph.update({ ('D', 'G'): color_constraint})
        graph.update({ ('D', 'C'): color_constraint})
        
        graph.update({ ('E', 'A'): color_constraint})
        graph.update({ ('E', 'D'): color_constraint})
        graph.update({ ('E', 'F'): color_constraint})
        graph.update({ ('E', 'G'): color_constraint})
        
        graph.update({ ('F', 'A'): color_constraint})
        graph.update({ ('F', 'B'): color_constraint})
        graph.update({ ('F', 'C'): color_constraint})
        graph.update({ ('F', 'G'): color_constraint})
        graph.update({ ('F', 'E'): color_constraint})
        
        graph.update({ ('G', 'F'): color_constraint})
        graph.update({ ('G', 'C'): color_constraint})
        graph.update({ ('G', 'E'): color_constraint})
        graph.update({ ('G', 'D'): color_constraint})
        return graph
    
    else:
        return None
    

def make_domains(n):
    
    if n == 'b':
        region.append('F')
    
    elif n == 'c':
        region.append('F')
        region.append('G')
        
    return { r:colors for r in region }

cs = ConstraintSearch(make_domains('a'), make_constraint_graph('a'))
print(cs.search())

cs = ConstraintSearch(make_domains('b'), make_constraint_graph('b'))
print(cs.search())

cs = ConstraintSearch(make_domains('c'), make_constraint_graph('c'))
print(cs.search())

