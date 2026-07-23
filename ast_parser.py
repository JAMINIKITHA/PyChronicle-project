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

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.Import):
            for item in node.names:
                imports.append(item.name)

        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

    print("Functions:", functions)
    print("Classes:", classes)
    print("Imports:", imports)


print("Tree created")

tree = parse_python_file("sample.py")

print("Calling extractor")

extract_details(tree)