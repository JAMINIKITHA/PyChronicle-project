import ast

print("AST Parser Running")


def parse_python_file(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())
    return tree


def extract_details(tree):
    functions = []
    classes = []
    imports = []
    variables = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.Import):
            for item in node.names:
                imports.append(item.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables.append(target.id)

    print("Functions:", functions)
    print("Classes:", classes)
    print("Imports:", imports)
    print("Variables:", variables)


def calculate_metrics(tree):
    functions = 0
    classes = 0
    imports = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions += 1

        elif isinstance(node, ast.ClassDef):
            classes += 1

        elif isinstance(node, ast.Import):
            imports += 1

        elif isinstance(node, ast.ImportFrom):
            imports += 1

    with open("sample.py", "r") as file:
        total_lines = len(file.readlines())

    print("code Metrics:")
    print("Functions:", functions)
    print("Classes:", classes)
    print("Imports:", imports)
    print("Total Lines:", total_lines)


tree = parse_python_file("sample.py")

extract_details(tree)

calculate_metrics(tree)