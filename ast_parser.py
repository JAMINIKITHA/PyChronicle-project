import ast
import sys
import sqlite3

print("AST Parser Running")
def create_database():
    conn = sqlite3.connect("pychronicle.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS variable_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        line_number INTEGER,
        variable_name TEXT,
        variable_value TEXT
    )
    """)

    conn.commit()
    conn.close()
    create_database()
def trace_calls(frame, event, arg):
    print(f"Line: {frame.f_lineno}")
    return trace_calls
sys.settrace(trace_calls)
print("Tracer Started")

def parse_python_file(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())
    return tree


def extract_details(tree):
    functions = []
    function_args = {}
    classes = []
    imports = []
    variables = [] 
    variable_lines = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
            function_args[node.name] = []

            for arg in node.args.args:
                function_args[node.name].append(arg.arg)

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
            variable_lines[target.id] = node.lineno

        

    print("Functions:", functions)
    print("Classes:", classes)
    print("Imports:", imports)
    print("Variables:", variables)
    print("Function Arguments:", function_args)
    print("Variable Line Numbers:", variable_lines)


def calculate_metrics(tree):
    functions = 0
    classes = 0
    imports = 0
    variables = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions += 1

        elif isinstance(node, ast.ClassDef):
            classes += 1

        elif isinstance(node, ast.Import):
            imports += 1

        elif isinstance(node, ast.ImportFrom):
            imports += 1

        elif isinstance(node, ast.Assign):
            variables += 1

    with open("sample.py", "r") as file:
        total_lines = len(file.readlines())

    print("Code Metrics:")
    print("Functions:", functions)
    print("Classes:", classes)
    print("Imports:", imports)
    print("Variables:", variables)
    print("Total Lines:", total_lines)

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = "sample.py"

tree = parse_python_file(file_name)

extract_details(tree)

calculate_metrics(tree)