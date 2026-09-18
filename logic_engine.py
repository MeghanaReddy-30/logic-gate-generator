import itertools
import pandas as pd
import graphviz
from sympy import sympify, Symbol, And, Or, Not

def parse_expression(expr_str):
    formatted_str = expr_str.replace("AND", "&").replace("OR", "|").replace("NOT", "~")
    return sympify(formatted_str)

def generate_truth_table(expr):
    vars_sorted = sorted(list(expr.free_symbols), key=lambda x: x.name)
    num_vars = len(vars_sorted)
    combinations = list(itertools.product([0, 1], repeat=num_vars))
    
    rows = []
    for combo in combinations:
        # Map inputs to standard SymPy booleans
        val_map = {var: bool(val) for var, val in zip(vars_sorted, combo)}
        
        # Evaluate expression using .subs()
        evaluated = expr.subs(val_map)
        
        # Convert SymPy's BooleanTrue/BooleanFalse into integer 1 or 0
        result = 1 if bool(evaluated) else 0
        
        rows.append(list(combo) + [result])
        
    cols = [v.name for v in vars_sorted] + [str(expr)]
    return pd.DataFrame(rows, columns=cols)
def build_circuit_graph(expr):
    dot = graphviz.Digraph(comment='Logic Circuit', graph_attr={'rankdir': 'LR'})
    node_counter = 0

    def add_node(subexpr):
        nonlocal node_counter
        current_id = f"node_{node_counter}"
        node_counter += 1

        if isinstance(subexpr, Symbol):
            dot.node(current_id, label=subexpr.name, shape='square', style='filled', fillcolor='lightgray')
            return current_id
        elif isinstance(subexpr, And):
            dot.node(current_id, label='AND', shape='rect', style='rounded,filled', fillcolor='lightblue')
            for arg in subexpr.args:
                child_id = add_node(arg)
                dot.edge(child_id, current_id)
            return current_id
        elif isinstance(subexpr, Or):
            dot.node(current_id, label='OR', shape='rect', style='rounded,filled', fillcolor='lightgreen')
            for arg in subexpr.args:
                child_id = add_node(arg)
                dot.edge(child_id, current_id)
            return current_id
        elif isinstance(subexpr, Not):
            dot.node(current_id, label='NOT', shape='triangle', style='filled', fillcolor='salmon')
            child_id = add_node(subexpr.args[0])
            dot.edge(child_id, current_id)
            return current_id
        return current_id

    root_id = add_node(expr)
    output_id = f"node_{node_counter}"
    dot.node(output_id, label="OUTPUT", shape='circle', style='filled', fillcolor='gold')
    dot.edge(root_id, output_id)

    return dot