import ast
from collections import defaultdict


class AssignmentCollector(ast.NodeVisitor):
    def __init__(self):
        self.line2vars = defaultdict(set)

    def visit_Assign(self, node):
        for t in node.targets:
            if isinstance(t, ast.Subscript):
                self.line2vars[node.lineno].add(t.value.id)
            elif isinstance(t, ast.Attribute):
                self.line2vars[node.lineno].add(t.value.id)
            else:
                self.line2vars[node.lineno].add(t.id)
        self.generic_visit(node)
