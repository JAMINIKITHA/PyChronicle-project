import ast

def parse_python_file(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())
    return tree

print("AST Parser Ready")