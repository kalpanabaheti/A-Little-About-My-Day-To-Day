import ast


class UserNamesCollector(ast.NodeVisitor):
    def __init__(self):
        self.user_names = set()

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.user_names.add(target.id)
            elif isinstance(target, ast.Subscript):
                self.user_names.add(target.value.id)
            elif isinstance(target, ast.Tuple):
                for tar in target.elts:
                    self.user_names.add(tar.id)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.user_names.add(node.name)
        for arg in node.args.args:
            self.user_names.add(arg.arg)
        self.generic_visit(node)

    def visit_For(self, node):
        if isinstance(node.target, ast.Tuple):
            print()
        else:
            self.user_names.add(node.target.id)
        self.generic_visit(node)

    # TODO: Comprehension lists. Lambdas...?
    def visit_ListComp(self, node):
        for gen in node.generators:
            if hasattr(gen.target, "elts"):
                for v in gen.target.elts:
                    self.user_names.add(v.id)
            else:
                self.user_names.add(gen.target.id)
        self.generic_visit(node)


if __name__ == "__main__":
    import ast

    program = "[(v, k) for v, k in {1: 2}]"
    tree = ast.parse(program)
    unc = UserNamesCollector()
    unc.visit(tree)
    print(unc.user_names)
